# Experiment 9
# Title: File Handling and I/O - Reading/writing files (CSV and JSON)

import csv
import json

input_file = r"C:\Users\Asus\OneDrive\Desktop\PL Experiments\APP\input.csv"
output_file = r"C:\Users\Asus\OneDrive\Desktop\PL Experiments\APP\output.json"

with open(input_file, "r") as file:
    data = csv.DictReader(file)
    records = list(data)

with open(output_file, "w") as file:
    json.dump(records, file, indent=4)

print("CSV data converted to JSON successfully.")