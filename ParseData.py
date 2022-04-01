import csv


def parse_csv(file_name):

    all_rows = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            all_rows.append(row)

    titles_row = all_rows.pop(0)
