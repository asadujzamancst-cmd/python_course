import csv

data = [
    ["Charlie", 60000, "System Administrator", "IT", "Chicago"],
    ["David", 95000, "Product Manager", "Product", "Boston"],
    ["Eve", 72000, "UX Designer", "Design", "Los Angeles"]
]

# Store CSV
csv_path = "example.csv"

with open(csv_path, mode="w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)   # writerows()

# Read CSV
data2 = []

with open(csv_path, mode="r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        data2.append(row)

print("List from CSV:")
for row in data2:
    print(row)