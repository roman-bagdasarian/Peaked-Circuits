import argparse
import sys
from qiskit import QuantumCircuit
from helpers.tee import Tee

def main():
    parser = argparse.ArgumentParser(description="Analyse circuit")
    parser.add_argument("path", help="Path to .qasm file")
    args = parser.parse_args()

    try:
        original_stdout = sys.stdout
        sys.stdout = Tee(f"{args.path}.txt")

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

    finally:
        if isinstance(sys.stdout, Tee):
            sys.stdout.log.close()
            sys.stdout = original_stdout
        sys.stdout.close()


if __name__ == "__main__":
    main()
