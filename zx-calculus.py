import argparse
from qiskit import QuantumCircuit, transpile, qasm2
import pyzx as zx
from helpers.utils import timer


def main():
    parser = argparse.ArgumentParser(description="ZX-Calculus")
    parser.add_argument("path", help="Path to .qasm file")
    args = parser.parse_args()

    try:
        qc = QuantumCircuit.from_qasm_file(args.path)
        print(f"Original depth: {qc.depth()}, Gates: {dict(qc.count_ops())}")

        with timer("ZX-Calculus"):
            graph = zx.Circuit.from_qasm(qasm2.dumps(qc)).to_graph()
            zx.full_reduce(graph)
            zx_circuit = QuantumCircuit.from_qasm_str(
                zx.extract_circuit(graph).to_qasm()
            )

        with timer("Circuit transpilation"):
            transpiled_circuit = transpile(
                zx_circuit, basis_gates=["u3", "cx"], optimization_level=3
            )

        print(
            f"Optimized depth: {transpiled_circuit.depth()}, Gates: {dict(transpiled_circuit.count_ops())}"
        )

        with open("zx-calculus.qasm", "w") as f:
            qasm2.dump(transpiled_circuit, f)

    except FileNotFoundError:
        print(f"Error: File '{args.path}' not found.")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
