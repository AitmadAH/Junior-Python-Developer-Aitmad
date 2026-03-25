import csv
import json
import os


def create_sample_csv(file_path: str) -> None:
    sample_data = [
        ["id", "name", "email", "age"],
        ["1", "Alice", "alice@example.com", "25"],
        ["2", "Bob", "bob@example.com", "30"],
        ["3", "Charlie", "charlie@example.com", "22"],
        ["4", "Diana", "diana@example.com", "28"],
    ]

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)

    print(f"Sample CSV file '{file_path}' has been created.")


def csv_to_json(csv_file_path: str, json_file_path: str) -> None:
    try:
        data = []

        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'.")

    except FileNotFoundError:
        print("CSV file not found. Creating a sample CSV file...")
        create_sample_csv(csv_file_path)
        csv_to_json(csv_file_path, json_file_path)


if __name__ == '__main__':
    sample_csv = 'users.csv'
    output_json = 'users.json'

    csv_to_json(sample_csv, output_json)

