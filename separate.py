from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import networkx as nx

qc = QuantumCircuit.from_qasm_file(r"MIT iQuHACK 2026\P7_rolling_ridge.qasm")
num_qubits = qc.num_qubits

print("=== Factoring Quantum Circuit ===")

G = nx.Graph()
G.add_nodes_from(range(num_qubits))

for instr in qc.data:
    if len(instr.qubits) == 2:
        G.add_edge(instr.qubits[0]._index, instr.qubits[1]._index)

comps = list(nx.connected_components(G))
print(f"Components found: {len(comps)} (Sizes: {[len(c) for c in comps]})\n")

qubit_map = {}
for c_idx, comp in enumerate(comps):
    for rel_idx, abs_idx in enumerate(sorted(list(comp))):
        qubit_map[abs_idx] = (c_idx, rel_idx)

sub_circuits = [QuantumCircuit(len(c)) for c in comps]

for instr in qc.data:
    q_indices = [q._index for q in instr.qubits]
    c_idx = qubit_map[q_indices[0]][0]
    rel_indices = [qubit_map[q][1] for q in q_indices]
    sub_circuits[c_idx].append(instr.operation, rel_indices)

comp_winners = []
sim_mps = AerSimulator(method="statevector")

for i, sub_qc in enumerate(sub_circuits):
    print(f"Solving Split {i + 1}/{len(comps)} ({sub_qc.num_qubits} qubits)...")
    sub_qc.measure_all()
    t_sub = transpile(sub_qc, sim_mps)
    job = sim_mps.run(t_sub, shots=1024)
    counts = job.result().get_counts()
    winner = max(counts, key=counts.get)
    probability = counts[winner] / 1024
    print(f"  └─ Bitstring: {winner} (Probability: {probability:.4f})")
    comp_winners.append(winner)

final_bits = [""] * num_qubits
for abs_idx in range(num_qubits):
    c_idx, rel_idx = qubit_map[abs_idx]
    final_bits[abs_idx] = comp_winners[c_idx][-(rel_idx + 1)]

final_solution = "".join(final_bits[::-1])
print(f"\n[FINAL SOLUTION]: {final_solution}")