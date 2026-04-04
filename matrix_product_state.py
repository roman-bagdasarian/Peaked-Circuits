from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


simulator = AerSimulator(
    method="matrix_product_state", matrix_product_state_max_bond_dimension=64
)
quantum_circuit = QuantumCircuit.from_qasm_file("<YOUR_RELATIVE_PATH>")

quantum_circuit.measure_all()
transpiled_circuit = transpile(quantum_circuit, simulator)

job_result = simulator.run(transpiled_circuit, shots=1024).result()
counts = job_result.get_counts()

print(max(counts, key=counts.get))
