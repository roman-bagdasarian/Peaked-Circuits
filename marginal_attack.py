import argparse
import sys
import numpy as np
from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit.quantum_info import SparsePauliOp
from helpers.tee import Tee
from helpers.utils import timer


def main():
    parser = argparse.ArgumentParser(
        description="MPS marginal attack: determine peak bitstring from single-qubit "
        "Z expectation values"
    )
    parser.add_argument("path", help="Path to .qasm file")
    parser.add_argument(
        "--bond_dim",
        type=int,
        default=64,
        help="Max bond dimension for MPS. Default: 64",
    )
    parser.add_argument(
        "--optimization_level",
        type=int,
        default=3,
        choices=[0, 1, 2, 3],
        help="Qiskit PassManager optimization level. Default: 3",
    )
    parser.add_argument(
        "--approx_degree",
        type=float,
        default=0.99,
        help="Approximate synthesis degree. Default: 0.99",
    )
    args = parser.parse_args()

    try:
        original_stdout = sys.stdout
        sys.stdout = Tee(f"{args.path}.txt")

        qc = QuantumCircuit.from_qasm_file(args.path)
        n = qc.num_qubits
        print(f"Loaded circuit: {n} qubits")

        # Remove measurements and optimize
        qc.remove_final_measurements(inplace=True)

        with timer("PassManager optimization"):
            pm = generate_preset_pass_manager(
                optimization_level=args.optimization_level,
                basis_gates=["u3", "cz"],
                approximation_degree=args.approx_degree,
            )
            qc_opt = pm.run(qc)

        orig_gates = sum(
            v for k, v in qc.count_ops().items() if k not in ("measure", "barrier")
        )
        opt_gates = sum(
            v
            for k, v in qc_opt.count_ops().items()
            if k not in ("measure", "barrier")
        )
        reduction = 100 * (1 - opt_gates / orig_gates) if orig_gates > 0 else 0
        print(
            f"PassManager: {orig_gates} -> {opt_gates} gates "
            f"({reduction:.1f}% reduction), "
            f"depth {qc.depth()} -> {qc_opt.depth()}"
        )

        # Build circuit with all Z expectation value saves
        qc_obs = qc_opt.copy()
        for i in range(n):
            pauli_str = ["I"] * n
            pauli_str[n - 1 - i] = "Z"
            op = SparsePauliOp("".join(pauli_str))
            qc_obs.save_expectation_value(op, list(range(n)), label=f"z_{i}")

        # Run single MPS simulation
        sim = AerSimulator(method="matrix_product_state")
        print(
            f"Running MPS marginal attack "
            f"(bond_dim={args.bond_dim}, {n} observables)..."
        )
        sys.stdout.flush()

        with timer("MPS simulation"):
            result = sim.run(
                qc_obs,
                matrix_product_state_max_bond_dimension=args.bond_dim,
            ).result()

        # Extract Z expectation values
        z_expvals = []
        for i in range(n):
            exp_val = result.data().get(f"z_{i}", 0.0)
            if hasattr(exp_val, "real"):
                exp_val = exp_val.real
            z_expvals.append(float(exp_val))

        z_expvals = np.array(z_expvals)
        bits = (z_expvals < 0).astype(int)

        # bits[i] = bit for qubit i (little-endian: q0 first)
        # Qiskit measurement convention is big-endian: q_{n-1} first
        peak_le = "".join(str(b) for b in bits)  # little-endian (q0 first)
        peak_be = peak_le[::-1]  # big-endian (q_{n-1} first)

        min_z = float(np.min(np.abs(z_expvals)))
        mean_z = float(np.mean(np.abs(z_expvals)))
        weak = sum(1 for z in z_expvals if abs(z) < 0.1)

        print(f"Little-Endian: {peak_le}")
        print(f"Big-Endian   : {peak_be}")
        print(f"Min|<Z>|={min_z:.4f}, Mean|<Z>|={mean_z:.4f}, Weak={weak}/{n}")

    except FileNotFoundError:
        print(f"Error: File '{args.path}' not found.")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        if isinstance(sys.stdout, Tee):
            sys.stdout.log.close()
            sys.stdout = original_stdout


if __name__ == "__main__":
    main()
