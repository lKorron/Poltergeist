import numpy as np

def load_points(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = line.split()
            points.append([float(x), float(y)])
    return points


def load_density(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            points.append(float(line.strip()))
    return points



