def get_majority_string():
    bitstrings = []
    print("Enter your bitstrings (type 'done' to finish):")

    while True:
        entry = input(f"String #{len(bitstrings) + 1}: ").strip()

        if entry.lower() == "done":
            break

        if not all(char in "01" for char in entry):
            print("Invalid input. Please use only '0' and '1'.")
            continue

        if bitstrings and len(entry) != len(bitstrings[0]):
            print(f"Error: String must be length {len(bitstrings[0])}.")
            continue

        bitstrings.append(entry)

    final_bits = []
    num_bits = len(bitstrings[0])

    for i in range(num_bits):
        column = [s[i] for s in bitstrings]
        ones = column.count("1")
        zeros = column.count("0")

        if ones > zeros:
            final_bits.append("1")
        else:
            final_bits.append("0")

    return "".join(final_bits)


result = get_majority_string()
print(f"\nFinal Majority Bitstring: {result}")
