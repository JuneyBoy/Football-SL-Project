import csv


def parse_csv(file_name):

    all_rows = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        if file_name == "Raw Data/Standings.csv":
            for row in reader:
                all_rows.append(row[1])
        else:
            for row in reader:
                all_rows.append(row[3:])

    all_rows.pop(0)

    return all_rows


def parse_defensive_advanced(stats, i):
    all_rows = parse_csv("Raw Data/DefensiveAdvanced.csv")
    # Quarterback (QB) pressures per drop back
    stats[i] = [float(row[14].strip("%")) / 100 for row in all_rows]


def parse_defensive_drives(stats, i):
    all_rows = parse_csv("Raw Data/DefensiveDrives.csv")
    # percentage of offensive drives ending in score
    stats[i] = [float(row[2].strip("%")) / 100 for row in all_rows]
    # percentage of offensive drives ending in turnover
    stats[i + 1] = [float(row[3].strip("%")) / 100 for row in all_rows]


def parse_defensive_passing(stats, i):
    all_rows = parse_csv("Raw Data/DefensivePassing.csv")
    # percentage of attempted passes by offensive team intercepted
    stats[i] = [float(row[8].strip("%")) / 100 for row in all_rows]


def parse_offensive_drives(stats, i):
    all_rows = parse_csv("Raw Data/OffensiveDrives.csv")
    # percentage of offensive drives ending in score
    stats[i] = [float(row[2].strip("%")) / 100 for row in all_rows]
    # percentage of offensive drives ending in turnover
    stats[i + 1] = [float(row[3].strip("%")) / 100 for row in all_rows]
    # avg number of points scored per drive
    stats[i + 2] = [float(row[8]) for row in all_rows]


def parse_offensive_passing(stats, i):
    all_rows = parse_csv("Raw Data/OffensivePassing.csv")
    # pass completion
    stats[i] = [float(row[2].strip("%")) / 100 for row in all_rows]
    # adjusted yards gained per pass attempt
    stats[i + 1] = [float(row[10]) for row in all_rows]


def parse_offensive_rushing(stats, i):
    all_rows = parse_csv("Raw Data/OffensiveRushing.csv")
    # percentage of attempted passes by offensive team intercepted
    stats[i] = [float(row[4]) for row in all_rows]


stats = [0] * 11
parse_defensive_advanced(stats, 0)
parse_defensive_drives(stats, 1)
parse_defensive_passing(stats, 3)
parse_offensive_drives(stats, 4)
parse_offensive_passing(stats, 7)
parse_offensive_rushing(stats, 9)
stats[10] = parse_csv("Raw Data/Standings.csv")
