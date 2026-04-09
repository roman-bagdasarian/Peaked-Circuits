import argparse
import sys
from qiskit import QuantumCircuit, transpile, qasm2
from helpers.tee import Tee


def main():
    parser = argparse.ArgumentParser(description="Approximate transpilation")
    parser.add_argument("path", help="Path to .qasm file")
    args = parser.parse_args()

    try:
        original_stdout = sys.stdout
        sys.stdout = Tee(f"{args.path}_transpiled.txt")

        qc = QuantumCircuit.from_qasm_file(args.path)
        print(f"Original depth: {qc.depth()}, Gates: {dict(qc.count_ops())}")

        results = {}
        degrees = (1, 0.99, 0.95)

        for degree in degrees:
            transpiled_circuit = transpile(
                qc,
                basis_gates=["u3", "cx"],
                approximation_degree=degree,
                optimization_level=3,
            )

            new_depth = transpiled_circuit.depth()
            results[degree] = transpiled_circuit

            print(
                f"Degree: {degree}, Optimized depth: {new_depth}, Gates: {dict(transpiled_circuit.count_ops())}"
            )

        choice = input(
            "Enter the degree you wish to save (e.g., 0.95) or press Enter to skip: "
        ).strip()

        if choice:
            try:
                selected_degree = float(choice)

                if selected_degree in results:
                    with open(f"{args.path}_transpiled.qasm", "w") as f:
                        qasm2.dump(results[selected_degree], f)

                else:
                    print(
                        f"Error: {selected_degree} was not one of the processed degrees."
                    )

            except ValueError:
                print("Error: Please enter a valid numerical degree.")

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
