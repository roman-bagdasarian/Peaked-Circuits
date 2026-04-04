from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


simulator = AerSimulator(method="matrix_product_state")
quantum_circuit = QuantumCircuit.from_qasm_file("<YOUR_RELATIVE_PATH>")

depth = quantum_circuit.depth()

for degree in (1.0, 0.99, 0.95, 0.90):
    transpiled_circuit = transpile(
        quantum_circuit,
        basis_gates=["u3", "cx"],
        approximation_degree=degree,
        optimization_level=3,
    )
    new_depth = transpiled_circuit.depth()

    if new_depth < 20:
        transpiled_circuit.measure_all(add_bits=False)
        job_result = simulator.run(transpiled_circuit, shots=1024).result()
        counts = job_result.get_counts()

        print(max(counts, key=counts.get))

        break
