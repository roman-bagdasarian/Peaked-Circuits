import argparse
import sys
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from helpers.tee import Tee
from helpers.utils import timer


def main():
    parser = argparse.ArgumentParser(description="Statevector/MPS simulation")
    parser.add_argument("path", help="Path to .qasm file")
    parser.add_argument(
        "--method",
        choices=["statevector", "matrix_product_state"],
        default="statevector",
        help="Simulation method. Default: statevector",
    )
    parser.add_argument(
        "--bond_dim",
        type=int,
        default=32,
        help="Max bond dimension for Matrix Product State. Default: 32",
    )
    args = parser.parse_args()

    try:
        original_stdout = sys.stdout
        sys.stdout = Tee(f"{args.path}.txt")

        if args.method == "matrix_product_state":
            simulator = AerSimulator(
                method="matrix_product_state",
                matrix_product_state_max_bond_dimension=args.bond_dim,
            )
            print(
                f"Using simulator method: {args.method} with bond dimension {args.bond_dim}"
            )
        else:
            simulator = AerSimulator(method="statevector")
            print(f"Using simulator method: {args.method}")

        quantum_circuit = QuantumCircuit.from_qasm_file(args.path)
        quantum_circuit.measure_all()
        transpiled_circuit = transpile(quantum_circuit, simulator)

        with timer("Circuit simulation"):
            job_result = simulator.run(transpiled_circuit, shots=1024).result()
        counts = job_result.get_counts()

        peak_bitstring = max(counts, key=counts.get)
        print(
            f"Little-Endian: {peak_bitstring}",
            f"Big-Endian   : {peak_bitstring[::-1]}",
            sep="\n",
        )
        print(f"Probability  : {counts[peak_bitstring] / sum(counts.values())}")

    except FileNotFoundError:
        print(f"Error: File '{args.path}' not found.")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        if isinstance(sys.stdout, Tee):
            sys.stdout.log.close()
            sys.stdout = original_stdout
        sys.stdout.close()


if __name__ == "__main__":
    main()
