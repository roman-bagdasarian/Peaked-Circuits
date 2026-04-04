import pyzx as zx
from qiskit import QuantumCircuit, transpile, qasm2
from qiskit_aer import AerSimulator


quantum_circuit = QuantumCircuit.from_qasm_file("MIT iQuHACK 2026\P10_eternal_mountain.qasm")

graph = zx.Circuit.from_qasm(qasm2.dumps(quantum_circuit)).to_graph()
zx.full_reduce(graph)

zx_circuit = QuantumCircuit.from_qasm_str(zx.extract_circuit(graph).to_qasm())
zx_circuit.measure_all()

transpiled_circuit = transpile(
    zx_circuit, basis_gates=["u3", "cx"], optimization_level=3
)

simulator = AerSimulator(
    method="matrix_product_state", matrix_product_state_max_bond_dimension=128
)

job_result = simulator.run(transpiled_circuit, shots=1024).result()
counts = job_result.get_counts()

print(max(counts, key=counts.get))
