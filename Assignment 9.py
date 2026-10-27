import csv
import json

input_file = "input.csv"
output_file = "output.json"

data = []

try:
    with open(input_file, "r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open(output_file, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"CSV data has been converted to JSON and saved in '{output_file}'.")

except FileNotFoundError:
    print(f"Error: '{input_file}' not found.")
