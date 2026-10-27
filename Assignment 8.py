input_file = "input.txt"
output_file = "extracted_data.txt"

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    print("Total number of lines:", len(lines))

    first_two_lines = lines[:2]

    with open(output_file, "w") as file:
        file.writelines(first_two_lines)

    print("First two lines:")
    for line in first_two_lines:
        print(line, end="")

    print(f"\nExtracted data has been written to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: '{input_file}' not found.")
