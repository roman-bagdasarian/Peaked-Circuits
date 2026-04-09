# [Yale Quantum 2025](https://app.bluequbit.io/hackathons/wSvCWg8f38spoLm3)

All experiments were run on the 12th Gen Intel(R) Core(TM) i7-12700H.

---

## Problem 1: Little Peak 🌱

| Metric | Value |
|--------|-------|
| Qubits | 4 |
| Peaked Bitstring | `1001` |

**Command:**
```bash
python statevector.py --method statevector data/Yale_Quantum_2025/P1_little_peak.qasm
```

---

## Problem 2: Swift Rise 🌊

| Metric | Value |
|--------|-------|
| Qubits | 28 |
| Peaked Bitstring | `1100101101100011011000011100` |

**Command:**
```bash
python statevector.py --method statevector data/Yale_Quantum_2025/P2_swift_rise.qasm
```

---

## Problem 3: Sharp Peak 🏜️

| Metric | Value |
|--------|-------|
| Qubits | 44 |
| Peaked Bitstring | `10001101010101010000011111001101000100011010` |

**Command:**
```bash
python statevector.py --method matrix_product_state --bond_dim 64 data/Yale_Quantum_2025/P3_sharp_peak.qasm
```

---

## Problem 4: Golden Mountain ⛰️

| Metric | Value |
|--------|-------|
| Qubits | 48 |
| Peaked Bitstring | `011110000100001000000110101111110010100001111110` |

**Steps:**

1. Transpile circuit with degree = 0.95:
    ```bash
    python transpilation.py data/Yale_Quantum_2025/P4_golden_mountain.qasm
    ```

2. Simulate with increased bond dimension (128 instead of default 64):
    ```bash
    python statevector.py --method matrix_product_state --bond_dim 128 data/Yale_Quantum_2025/P4_golden_mountain.qasm_transpiled.qasm
    ```

    > Note: Due to very low probabilities, use `majority_voting.py` to sample the final bitstring multiple times for better accuracy.

---

## Problem 5: Granite Summit 🗻

| Metric | Value |
|--------|-------|
| Qubits | 44 |
| Peaked Bitstring | *Pending* |

---

## Problem 6: Titan Pinnacle 🌋

| Metric | Value |
|--------|-------|
| Qubits | 62 |
| Peaked Bitstring | *Pending* |
