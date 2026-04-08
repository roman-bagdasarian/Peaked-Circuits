# Peaked Circuits

**Peaked circuits** are pre-constructed quantum circuits with a non-uniform distribution of measurement outcomes. They are designed in a way that one particular bitstring has a higher probability than others, e.g. ```O(1)``` as opposed to exponentially small amplitude.

They were introduced by [Scott Aaronson][1] as a way to achieve verifiable quantum advantage. Carefully crafted peaked circuits look like random circuits  - like the one used by Google in their benchmark that would take supercomputers septillion```=10²⁵``` years to replicate. However, unlike random circuits - peaked circuits are much easier to verify: all you need to do is to run them on a quantum computer and verify you get the correct hidden bitstring!

## History of Development

- In April 2024, Scott Aaronson and Yuxuan Zhang first introduced Peaked Circuits as a "benchmark" for quantum computers.
- In April 2025, the first ever Peaked Circuits Hackathon took place at Yale!
- In January 2026, BlueQubit first introduced HQAP Circuits ([Heuristic Quantum Advantage with Peaked Circuits][2]).

## Technicalities
Peaked Circuits are special quantum circuits in ```.qasm``` [format](https://en.wikipedia.org/wiki/OpenQASM) where each circuit sets up a specific quantum state. Hidden within that state is a single bitstring that appears with high probability.

<img width="1031" alt="image" src="Screenshot_2025-02-28_at_7.34.59_PM.webp" />

In the example above, ```0110``` is the peak bitstring as it has comparatively much higher probability  to be measured than all the other bitstrings. And below you can find the .qasm file that prepared this state:

```
OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
x q[1];
x q[2];
ry(0.8*pi) q[0];
ry(0.8*pi) q[1];
ry(0.8*pi) q[2];
ry(0.8*pi) q[3];
```

# Development Setup
1. Clone this repository: `gh repo clone roman-bagdasarian/Peaked-Circuits`
2. Create a conda environment: `conda env create -f environment.yml`
3. Activate the your new environment: `conda activate pc`
4. Run a sample test: `python sample.py`
5. Your output should be `1001`
6. Enjoy! Thank you for considering contributing to this project!

# Preprocessing and Simulating
In general, all the scripts are designed to be run from command line. The default structure is:
`python <METHOD_NAME>.py <PATH_TO_QASM>`

1. Access the parameters of your circuits with the METHOD_NAME = `characteristics`
2. Preprosess your circuits. There are three main ways to do so:
- `zx-calculus`
- `separation`
- `transpilation`
3. Decide on the method to simulate your circuit:
- `statevector` - run your circuits locally. ≤ 29 qubits for --method = `statevector` and unlimited for --method = `matrix_product_state` (Max Bond Dimension trades off probability (hence, time) for accuracy)
- `bluequbit_cpu` - run your circuits via BlueQubit's API (≤ 34 qubits). -- = API --device = `cpu` (Google's most powerful statevector) and --device = `mpc.cpu`

# Data

For most of the circuits generously provided by BlueQubit, there is no way to verify your solution (a bitstring in little-endian convention, usually)
# [Yale Quantum 2025](https://app.bluequbit.io/hackathons/wSvCWg8f38spoLm3)

Ranked #1 among all Yale participants (In-Person and Virtual) at the first-ever Peaked Circuits Hackathon!

| Name | Yale Rank | World Rank | Score | Solved Problems | Time Penalty |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Roman Bagdasarian** | **#1** | #59/1603 | 80 | **3**/6 | 2.21h |

| Problem | Qubits | Peak Bitstring |
| :--- | :---: | :---: |
| **Problem 1: Little Peak 🌱** | 4 | `1001` |
| **Problem 2: Swift Rise 🌊** | 28 | |
| **Problem 3: Sharp Peak 🏜** | 44 | |
| **Problem 4: Golden Mountain ⛰️** | 48 | |
| **Problem 5: Granite Summit 🗻** | 44 | |
| **Problem 6: Titan Pinnacle 🌋** | 62 | |

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

# Acknowledgements

I would like to give credit to [BlueQubit's](https://www.bluequbit.io/) CEO [Hayk Tepanyan](https://www.linkedin.com/in/tehayk/) for introducing me to Quantum Computing in August 2024 at his [talk](https://www.youtube.com/live/-JpAm3lfQtI?si=ZfxVLRx5XswsCwkA&t=2770) in Yerevan, Armenia and to [Tan Jun Liang](https://github.com/poig).

# References
[1]: https://doi.org/10.48550/arXiv.2404.14493 "Aaronson, S., & Zhang, Y. (2024). On verifiable quantum advantage with peaked circuit sampling (arXiv:2404.14493). arXiv."

[2]: https://doi.org/10.48550/arXiv.2510.25838 "Gharibyan, H., Mullath, M. Z., Sherman, N. E., Su, V. P., Tepanyan, H., & Zhang, Y. (2025). Heuristic Quantum Advantage with Peaked Circuits (arXiv:2510.25838). arXiv."