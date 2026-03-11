import csv

input_file = "input.csv"
output_file = "output.csv"

with open(input_file, "r") as file:
  reader = csv.DictReader(file)

  filtered_data = []

  for row in reader:
    salary = int(row["salary"])

    if salary >= 3000:
      filtered_data.append(row)

with open(output_file, "w", newline="") as file:
    fieldnames = ["name", "age", "city", "salary"]
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(filtered_data)

print("Processamento concluído!")