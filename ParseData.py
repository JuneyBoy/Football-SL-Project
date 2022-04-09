import csv, operator


def parse_csv(file_name):

    all_rows = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            all_rows.append(row[3:])

    all_rows.pop(0)

    return all_rows


def parse_defensive_advanced(stats, file_name):
    all_rows = parse_csv(file_name)

    for i, row in enumerate(all_rows):
        # Quarterback (QB) pressures per drop back
        # print(str(i))
        stats[i][0] = float(row[14].strip("%")) / 100


def parse_defensive_drives(stats, file_name):
    all_rows = parse_csv(file_name)

    for i, row in enumerate(all_rows):
        # percentage of offensive drives ending in score
        stats[i][1] = float(row[2].strip("%")) / 100
        # percentage of offensive drives ending in turnover
        stats[i][2] = float(row[3].strip("%")) / 100


def parse_defensive_passing(stats, file_name):
    all_rows = parse_csv(file_name)

    for i, row in enumerate(all_rows):
        # percentage of attempted passes by offensive team intercepted
        stats[i][3] = float(row[8].strip("%")) / 100


def parse_offensive_drives(stats, file_name):
    all_rows = parse_csv(file_name)

    for i, row in enumerate(all_rows):
        # percentage of offensive drives ending in score
        stats[i][4] = float(row[2].strip("%")) / 100
        # percentage of offensive drives ending in turnover
        stats[i][5] = float(row[3].strip("%")) / 100
        # avg number of points scored per drive
        stats[i][6] = float(row[8]) / 100


def parse_offensive_passing(stats, file_name):
    all_rows = parse_csv(file_name)

    for i, row in enumerate(all_rows):
        # pass completion
        stats[i][7] = float(row[2].strip("%")) / 100
        # adjusted yards gained per pass attempt
        stats[i][8] = float(row[10])


def parse_offensive_rushing(stats, file_name):
    all_rows = parse_csv(file_name)

    for i, row in enumerate(all_rows):
        # yards gained per attempt
        stats[i][9] = float(row[4])


def get_wins(stats, file_name):
    wins = csv.reader(open(file_name), delimiter=",")
    # sorts each row by the Team Name
    wins = sorted(wins, key=operator.itemgetter(0))
    # gets rid of label row (which ends up being the 2nd to last row after sorting)
    wins.pop(-2)

    for i, row in enumerate(wins):
        stats[i][10] = float(row[1])


training_examples = [[0] * 11 for i in range(32)]
parse_defensive_advanced(training_examples, "Raw Data/2021_Data/DefensiveAdvanced.csv")
parse_defensive_drives(training_examples, "Raw Data/2021_Data/DefensiveDrives.csv")
parse_defensive_passing(training_examples, "Raw Data/2021_Data/DefensivePassing.csv")
parse_offensive_drives(training_examples, "Raw Data/2021_Data/DefensivePassing.csv")
parse_offensive_passing(training_examples, "Raw Data/2021_Data/OffensivePassing.csv")
parse_offensive_rushing(training_examples, "Raw Data/2021_Data/OffensiveRushing.csv")
get_wins(training_examples, "Raw Data/2021_Data/2021_Standings.csv")

validation_examples = [[0] * 11 for i in range(32)]
parse_defensive_advanced(
    validation_examples, "Raw Data/2020_Data/DefensiveAdvanced.csv"
)
parse_defensive_drives(validation_examples, "Raw Data/2020_Data/DefensiveDrives.csv")
parse_defensive_passing(validation_examples, "Raw Data/2020_Data/DefensivePassing.csv")
parse_offensive_drives(validation_examples, "Raw Data/2020_Data/DefensivePassing.csv")
parse_offensive_passing(validation_examples, "Raw Data/2020_Data/OffensivePassing.csv")
parse_offensive_rushing(validation_examples, "Raw Data/2020_Data/OffensiveRushing.csv")
get_wins(validation_examples, "Raw Data/2020_Data/2020_Standings.csv")

# print(training_examples)
print(validation_examples[0])
