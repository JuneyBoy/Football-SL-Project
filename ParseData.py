import csv


def parse_csv(file_name):

    all_rows = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            all_rows.append(row[2:])

    all_rows.pop(0)

    return all_rows


def parse_defensive_advanced():
    all_rows = parse_csv("Raw Data/DefensiveAdvanced.csv")

    defensive_advanced_data = [float(row[15].strip("%")) / 100 for row in all_rows]

    print(defensive_advanced_data)
