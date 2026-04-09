import argparse
import sys
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import networkx as nx
from helpers.tee import Tee
from helpers.utils import timer

def main():
    parser = argparse.ArgumentParser(description="Separation into two circuits")
    parser.add_argument("path", help="Path to .qasm file")
    args = parser.parse_args()

    try:
        original_stdout = sys.stdout
        sys.stdout = Tee(f"{args.path}.txt")

        qc = QuantumCircuit.from_qasm_file(args.path)
        num_qubits = qc.num_qubits

        G = nx.Graph()
        G.add_nodes_from(range(num_qubits))

        for instr in qc.data:
            if len(instr.qubits) == 2:
                G.add_edge(instr.qubits[0]._index, instr.qubits[1]._index)

        components = list(nx.connected_components(G))
        print(f"{len(components)} components of sizes {[len(c) for c in components]}\n")

        qubit_map = {}
        for c_idx, comp in enumerate(components):
            for rel_idx, abs_idx in enumerate(sorted(list(comp))):
                qubit_map[abs_idx] = (c_idx, rel_idx)

        sub_circuits = [QuantumCircuit(len(c)) for c in components]

        for instr in qc.data:
            q_indices = [q._index for q in instr.qubits]
            c_idx = qubit_map[q_indices[0]][0]
            rel_indices = [qubit_map[q][1] for q in q_indices]
            sub_circuits[c_idx].append(instr.operation, rel_indices)

        component_results = []
        simulator = AerSimulator(method="statevector")

        for i, sub_qc in enumerate(sub_circuits):
            print(f"Simulating component {i + 1}")

            sub_qc.measure_all()
            transpiled_circuit = transpile(sub_qc, simulator)

            with timer("Circuit simulation"):
                job_result = simulator.run(transpiled_circuit, shots=1024).result()
            counts = job_result.get_counts()

            peak_bitstring = max(counts, key=counts.get)
            print(
                f"Little-Endian: {peak_bitstring}",
                f"Big-Endian   : {peak_bitstring[::-1]}",
                sep="\n",
            )
            print(f"Probability  : {counts[peak_bitstring] / sum(counts.values())}\n")
            component_results.append(peak_bitstring)

        final_bits = [""] * num_qubits
        for abs_idx in range(num_qubits):
            c_idx, rel_idx = qubit_map[abs_idx]
            final_bits[abs_idx] = component_results[c_idx][-(rel_idx + 1)]

        peak_bitstring = "".join(final_bits[::-1])

        print(
            f"Little-Endian: {peak_bitstring}",
            f"Big-Endian   : {peak_bitstring[::-1]}",
            sep="\n",
        )

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
