import argparse
from qiskit import QuantumCircuit


def main():
    parser = argparse.ArgumentParser(description="Analyse circuit")
    parser.add_argument("path", help="Path to .qasm file")
    args = parser.parse_args()

    try:
        qc = QuantumCircuit.from_qasm_file(args.path)

        stats = {
            "qubits": qc.num_qubits,
            "depth": qc.depth(),
            "ops": qc.count_ops(),
            "size": qc.size(),
            "multi-qubit gates": qc.num_nonlocal_gates(),
        }
        print(stats)

    except FileNotFoundError:
        print(f"Error: File '{args.path}' not found.")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
