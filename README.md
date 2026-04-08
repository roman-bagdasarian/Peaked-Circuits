# Peaked Circuits

In January 2026, BlueQubit first introduced HQAP Circuits (Heuristic Quantum Advantage with Peaked Circuits).

Gharibyan, H., Mullath, M. Z., Sherman, N. E., Su, V. P., Tepanyan, H., & Zhang, Y. (2025). Heuristic Quantum Advantage with Peaked Circuits (arXiv:2510.25838). arXiv. https://doi.org/10.48550/arXiv.2510.25838

# Development Setup
1. Clone this repository: `gh repo clone roman-bagdasarian/Peaked-Circuits`
2. Create a conda environment: `conda env create -f environment.yml`
3. Activate the your new environment: `conda activate pc`
4. Run a sample test: `python sample.py`
5. Your output should be `1001`
6. Enjoy! Thank you for considering contributing to this project!

# Limitations

## Qubits
`statevector.py` ≤ 29 qubits
`bluequbit_cpu.py` ≤ 34 qubits

## Accuracy
`matrix_product_state.py` = Max Bond Dimension trades off probability (hence, time) for accuracy

# [Yale Quantum 2025](https://app.bluequbit.io/hackathons/wSvCWg8f38spoLm3)

Ranked #1 among all Yale participants (In-Person and Virtual) at the first-ever Peaked Circuits Hackathon!

| Name | Yale Rank | World Rank | Score | Solved Problems | Time Penalty |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Roman Bagdasarian** | **#1** | #59/1603 | 80 | **3**/6 | 2.21h |

| Problem | Qubits | Peak Bitstring |
| :--- | :---: | :---: |
| **Problem 1: Little Peak 🌱** | 4 | `1001` |
| **Problem 2: Swift Rise 🌊** | 28 | `` |
| **Problem 3: Sharp Peak 🏜** | 44 | `` |
| **Problem 4: Golden Mountain ⛰️** | 48 | `` |
| **Problem 5: Granite Summit 🗻** | 44 | `` |
| **Problem 6: Titan Pinnacle 🌋** | 62 | `` |

# [MIT iQuHACK 2026](https://app.bluequbit.io/hackathons/QlLEye0ap4l4zXX2)

| Name | World Rank | Score | Solved Problems | Time Penalty |
| :--- | :---: | :---: | :---: | :---: |
| **Roman Bagdasarian** | **#63**/550 | 230 | **6**/10 | 25.21h |

| Problem | Qubits | Peak Bitstring |
| :--- | :---: | :---: |
| **Problem 1: Little Dimple 🫧** | 4 | `1001` |
| **Problem 2: Small Bump 🪨** | 12 | `00011000100010000011` |
| **Problem 3: Tiny Ripple 🌊** | 30 | `100010101100001101111100011100` |
| **Problem 4: Gentle Mound 🌿** | 40 | `0110101000010111001100100001010001101101` |
| **Problem 5: Soft Rise 🌄** | 50 | `01101000100100001010101011100000010111100011111110` |
| **Problem 6: Low Hill ⛰️** | 60 | `000100010001101000100101110101010001111001000001000011000101` |
| **Problem 7: Rolling Ridge 🏞️** | 42 | `0110001011111111110011110001000010011011100000` |
| **Problem 8: Bold Peak 🏜** | 58 | `101111100101111000100010110001011101110011100011110000100111010010001010` |
| **Problem 9: Grand Summit 🏔️** | 69 | |
| **Problem 10: Eternal Mountain 🗻** | 56 | `00111111100000110001010111111001011101100001100100010010` |

# [Yale Quantum 2026](https://app.bluequbit.io/hackathons/wSvCWg8f38spoXX3)

| Team Name | World Rank | Score | Solved Problems | Time Penalty |
| :--- | :---: | :---: | :---: | :---: |
| **MerQury** | **#13**/550 | 450 | **9**/10 | 28.36h |

| Problem | Qubits | Peak Bitstring |
| :--- | :---: | :---: |
| **Problem 1: Little Dimple 🫧** | 4 | `1001` |
| **Problem 2: Small Bump 🪨** | 12 | `111010100110` |
| **Problem 3: Tiny Ripple 🌊** | 30 | `001111100001011001010111011000` |
| **Problem 4: Gentle Mound 🌿** | 40 | `0000111011000010110110011000010111001000` |
| **Problem 5: Soft Rise 🌄** | 50 | `00011011001101000001010110110100101010011000011001` |
| **Problem 6: Low Hill ⛰️** | 60 | `101100101001010001110111100101100011101011100000000000110111` |
| **Problem 7: Rolling Ridge 🏞️** | 42 | `001000110101110100110001000100001010101101` |
| **Problem 8: Bold Peak 🏜** | 58 | `0000000100000100110100010101001010001011111100100011001110` |
| **Problem 9: Grand Summit 🏔️** | 69 | `110001110111010101111000000010000111111111110011111111100101011100010` |
| **Problem 10: Eternal Mountain 🗻** | 56 | |
