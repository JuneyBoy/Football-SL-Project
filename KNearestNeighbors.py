import numpy as np
from ParseData import stats


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
        distances[example] = euclidean_distance(point_to_classify, example)

    # sorts dictionary by distances from least to greatest
    sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    print(sorted_distances)
    # keeps track of the sum of the outputs for the k-nearest neighbors
    sum = 0
    # keeps track of the weights of the k-nearest neighbors
    ws = []

    # for the k-nearest neighbors...
    for i in range(k):
        if weighted:
            wi = 1 / np.square(list(sorted_distances.values())[i])
            ws.append(wi)
            sum += wi * list(sorted_distances)[i][1]
        else:
            sum += list(sorted_distances)[i][1]

    # returns averages
    if weighted:
        return sum / np.sum(ws)
    else:
        return sum / k
