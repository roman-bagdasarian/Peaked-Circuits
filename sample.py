from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


simulator = AerSimulator(method="statevector")
quantum_circuit = QuantumCircuit.from_qasm_file("Yale Quantum 2025\P1_little_peak.qasm")

quantum_circuit.measure_all()
transpiled_circuit = transpile(quantum_circuit, simulator)

job_result = simulator.run(transpiled_circuit, shots=1024).result()
counts = job_result.get_counts()

print(max(counts, key=counts.get))
