import argparse
import bluequbit
from qiskit import QuantumCircuit


def main():
    parser = argparse.ArgumentParser(description="Bluequbit CPU simulation")
    parser.add_argument("path", help="Path to .qasm file")
    parser.add_argument("--id", required=True, help="Your Bluequbit API Token")
    parser.add_argument(
        "--device",
        default="mps.cpu",
        help="Target device (mps.cpu or cpu). Default: mps.cpu",
    )
    parser.add_argument(
        "--bond_dim",
        type=int,
        default=64,
        help="Max bond dimension for MPS simulations. Default: 64",
    )
    args = parser.parse_args()

    try:
        bq = bluequbit.init(args.id)

        quantum_circuit = QuantumCircuit.from_qasm_file(args.path)
        quantum_circuit.measure_all()

        run_options = {}
        if "mps" in args.device.lower():
            run_options["mps_bond_dimension"] = args.bond_dim

        job_result = bq.run(
            quantum_circuit,
            device=args.device,
            shots=1024,
            options=run_options,
        )
        counts = job_result.get_counts()

        peak_bitstring = max(counts, key=counts.get)
        print(
            f"Little-Endian: {peak_bitstring}",
            f"Big-Endian   : {peak_bitstring[::-1]}",
            sep="\n",
        )

    except FileNotFoundError:
        print(f"Error: File '{args.path}' not found.")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
