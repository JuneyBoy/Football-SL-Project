import csv, operator


def get_wins(file_name):
    wins = csv.reader(open(file_name), delimiter=",")
    wins = sorted(wins, key=operator.itemgetter(0))

    return [win[1] for win in wins]


def parse_csv(file_name):

    all_rows = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            all_rows.append(row[3:])

    all_rows.pop(0)

    return all_rows


def parse_defensive_advanced(stats, i, file_name):
    all_rows = parse_csv(file_name)
    # Quarterback (QB) pressures per drop back
    stats[i] = [float(row[14].strip("%")) / 100 for row in all_rows]


def parse_defensive_drives(stats, i, file_name):
    all_rows = parse_csv(file_name)
    # percentage of offensive drives ending in score
    stats[i] = [float(row[2].strip("%")) / 100 for row in all_rows]
    # percentage of offensive drives ending in turnover
    stats[i + 1] = [float(row[3].strip("%")) / 100 for row in all_rows]


def parse_defensive_passing(stats, i, file_name):
    all_rows = parse_csv(file_name)
    # percentage of attempted passes by offensive team intercepted
    stats[i] = [float(row[8].strip("%")) / 100 for row in all_rows]


def parse_offensive_drives(stats, i, file_name):
    all_rows = parse_csv(file_name)
    # percentage of offensive drives ending in score
    stats[i] = [float(row[2].strip("%")) / 100 for row in all_rows]
    # percentage of offensive drives ending in turnover
    stats[i + 1] = [float(row[3].strip("%")) / 100 for row in all_rows]
    # avg number of points scored per drive
    stats[i + 2] = [float(row[8]) for row in all_rows]


def parse_offensive_passing(stats, i, file_name):
    all_rows = parse_csv(file_name)
    # pass completion
    stats[i] = [float(row[2].strip("%")) / 100 for row in all_rows]
    # adjusted yards gained per pass attempt
    stats[i + 1] = [float(row[10]) for row in all_rows]


def parse_offensive_rushing(stats, i, file_name):
    all_rows = parse_csv(file_name)
    # percentage of attempted passes by offensive team intercepted
    stats[i] = [float(row[4]) for row in all_rows]


training_examples = [0] * 11
parse_defensive_advanced(
    training_examples, 0, "Raw Data/2021_Data/DefensiveAdvanced.csv"
)
parse_defensive_drives(training_examples, 1, "Raw Data/2021_Data/DefensiveDrives.csv")
parse_defensive_passing(training_examples, 3, "Raw Data/2021_Data/DefensivePassing.csv")
parse_offensive_drives(training_examples, 4, "Raw Data/2021_Data/DefensivePassing.csv")
parse_offensive_passing(training_examples, 7, "Raw Data/2021_Data/OffensivePassing.csv")
parse_offensive_rushing(training_examples, 9, "Raw Data/2021_Data/OffensiveRushing.csv")
training_examples[10] = get_wins("Raw Data/2021_Data/2021_Data/2021_Standings.csv")

validation_examples = [0] * 11
parse_defensive_advanced(
    training_examples, 0, "Raw Data/2020_Data/DefensiveAdvanced.csv"
)
parse_defensive_drives(training_examples, 1, "Raw Data/2020_Data/DefensiveDrives.csv")
parse_defensive_passing(training_examples, 3, "Raw Data/2020_Data/DefensivePassing.csv")
parse_offensive_drives(training_examples, 4, "Raw Data/2020_Data/DefensivePassing.csv")
parse_offensive_passing(training_examples, 7, "Raw Data/2020_Data/OffensivePassing.csv")
parse_offensive_rushing(training_examples, 9, "Raw Data/2020_Data/OffensiveRushing.csv")
validation_examples[10] = get_wins("Raw Data/2020_Data/2021_Data/2021_Standings.csv")
