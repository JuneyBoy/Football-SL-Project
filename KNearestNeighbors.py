import numpy as np
from ParseData import training_examples
from ParseData import validation_examples


def euclidean_distance(p1, p2):
    squares = 0

    # sums up the distance between each corresponding dimension of the coordinates
    for i in range(len(p1)):
        squares += np.square(p1[i] - p2[i])

    distance = np.sqrt(squares)
    return distance


def k_nearest_neighbors_real_value(k, point_to_classify, training_examples, weighted):

    # keys -> example, value -> distance
    distances = {}

    # get distances between each of the training examples and point_to_classify
    for example in training_examples:
        distances[tuple(example)] = euclidean_distance(point_to_classify, example)

    # sorts dictionary by distances from least to greatest
    sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    # print(sorted_distances)
    # keeps track of the sum of the outputs for the k-nearest neighbors
    sum = 0
    # keeps track of the weights of the k-nearest neighbors
    ws = []

    # for the k-nearest neighbors...
    for i in range(k):
        if weighted:
            wi = 1 / np.square(list(sorted_distances.values())[i])
            ws.append(wi)
            sum += wi * list(sorted_distances)[i][10]
        else:
            sum += list(sorted_distances)[i][10]

    # returns averages
    if weighted:
        return sum / np.sum(ws)
    else:
        return sum / k


# k_nearest_neighbors_real_value(
#     3, (validation_examples[0])[:-1], training_examples, True
# )

predicted_wins = [
    k_nearest_neighbors_real_value(3, team_data[:-1], training_examples, True)
    for team_data in validation_examples
]

print(
    [
        validation_example[-1] - predicted_win
        for validation_example, predicted_win in zip(
            validation_examples, predicted_wins
        )
    ]
)
