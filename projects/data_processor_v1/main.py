import csv

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"


def read_data(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def filter_salary(data, min_salary=3000):
    filtered = []

    for row in data:
        if int(row["salary"]) >= min_salary:
            filtered.append(row)

    return filtered


def write_data(file_path, data):
    fieldnames = ["name", "age", "city", "salary"]

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


def main():
    data = read_data(INPUT_FILE)

    filtered_data = filter_salary(data)

    write_data(OUTPUT_FILE, filtered_data)

    print("Processamento concluído!")


if __name__ == "__main__":
    main()