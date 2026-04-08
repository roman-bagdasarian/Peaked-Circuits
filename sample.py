import os
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from helpers.utils import timer


simulator = AerSimulator(method="statevector")

quantum_circuit = QuantumCircuit.from_qasm_file(
    os.path.join("data", "Yale_Quantum_2025", "P1_little_peak.qasm")
)
quantum_circuit.measure_all()
transpiled_circuit = transpile(quantum_circuit, simulator)

with timer("Circuit simulation"):
    job_result = simulator.run(transpiled_circuit, shots=1024).result()
counts = job_result.get_counts()

peak_bitstring = max(counts, key=counts.get)
print(
    f"Little-Endian: {peak_bitstring}",
    f"Big-Endian   : {peak_bitstring[::-1]}",
    sep="\n",
)
print(f"Probability  : {counts[peak_bitstring] / sum(counts.values())}")
