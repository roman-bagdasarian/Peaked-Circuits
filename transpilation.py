import argparse
from qiskit import QuantumCircuit, transpile, qasm2


def main():
    parser = argparse.ArgumentParser(description="Approximate transpilation")
    parser.add_argument("path", help="Path to .qasm file")
    args = parser.parse_args()

    try:
        qc = QuantumCircuit.from_qasm_file(args.path)
        print(f"Original depth: {qc.depth()}, Gates: {dict(qc.count_ops())}")

        results = {}
        degrees = (1.00, 0.99, 0.95, 0.90)

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
                    filename = f"transpiled_{selected_degree}.qasm"
                    with open(filename, "w") as f:
                        qasm2.dump(results[selected_degree], f)
                    print(f"Successfully saved to {filename}")

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


if __name__ == "__main__":
    main()
