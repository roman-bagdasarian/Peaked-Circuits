import bluequbit
from qiskit import QuantumCircuit


bq = bluequbit.init("<YOUR_ID>")
quantum_circuit = QuantumCircuit.from_qasm_file("<YOUR_RELATIVE_PATH>")

quantum_circuit.measure_all()

job_result = bq.run(quantum_circuit, device="<YOUR_DEVICE>", shots=1024)
counts = job_result.get_counts()

print(max(counts, key=counts.get))
