# Peaked Circuits

In January 2026, BlueQubit first introduced HQAP Circuits (Heuristic Quantum Advantage with Peaked Circuits).

Gharibyan, H., Mullath, M. Z., Sherman, N. E., Su, V. P., Tepanyan, H., & Zhang, Y. (2025). Heuristic Quantum Advantage with Peaked Circuits (arXiv:2510.25838). arXiv. https://doi.org/10.48550/arXiv.2510.25838

# Development Setup
1. Clone this repository: `gh repo clone roman-bagdasarian/Peaked-Circuits`
2. Create a conda environment: `conda env create -f environment.yml`
3. Activate the your new environment: `conda activate pc`
4. Run a sample test: `python sample.py`
5. Your output should be `1001`
Enjoy!

# Contributing to this Repo
First off, thank you for considering contributing to this project!

## How Can I Contribute?
* Implement class to measure time
* Implement class to output circuit metadata

# Limitations

## Qubits
`statevector.py` ≤ 29 qubits
`bluequbit_cpu.py` ≤ 34 qubits

## Accuracy
`matrix_product_state.py` = Max Bond Dimension trades off probability (hence, time) fpr accuracy

# MIT iQuHACK 2026

| Problem | Qubits | Peak Bitstring |
| :--- | :---: | :---: |
| **`P1_little_peak.qasm`** | 4 | `1001` |
| **`P2_small_bump.qasm`** | 20 | `11000001000100011000` |
| **`P3_tiny_ripple.qasm`** | 30 | `001110001111101100001101010001` |
| **`P4_gentle_mound.qasm`** | 40 | `0110101000010111001100100001010001101101` |
| **`P5_soft_rise.qasm`** | 50 | `01101000100100001010101011100000010111100011111110` |
| **`P6_low_hill.qasm`** | 60 | `101000110000100000100111100010101011101001000101100010001000` |
| **`P7_rolling_ridge.qasm`** | 46 | `0110001011111111110011110001000010011011100000` |
| **`P8_bold_peak.qasm`** | 72 | `101111100101111000100010110001011101110011100011110000100111010010001010` |
| **`P9_grand_summit.qasm`** | 56 | **NOT SOLVED** |
| **`P10_eternal_mountain.qasm`** | 56 | `00111111100000110001010111111001011101100001100100010010` |
