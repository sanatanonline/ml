import numpy as np
import pandas as pd

from pylab import rand


def activate(weights, inputs, bias):
    activation = 0
    for i in range(len(weights)):
        activation += weights[i] * inputs[i]
    return activation + bias


def logsigmoid(x):
    s = 1 / (1 + np.exp(-x))
    # ds = s * (1 - s)
    return s


def tansigmoid(x):
    t = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    # dt = 1 - t ** 2
    return t


def purelinear(x):
    return x


def sign(x):
    if x >= 0:
        return 1
    else:
        return -1


def relu(x):
    return max(0, x)


def hardtansigmoid(x):
    return max(min(x, 1), -1)


def generate_data(n):
    xb = (rand(n) * 2 - 1) / 2 - 0.5
    yb = (rand(n) * 2 - 1) / 2 + 0.5
    xr = (rand(n) * 2 - 1) / 2 + 0.5
    yr = (rand(n) * 2 - 1) / 2 - 0.5
    inputs = []
    for i in range(len(xb)):
        inputs.append([xb[i], yb[i], 1])
        inputs.append([xr[i], yr[i], -1])
    x1 = []
    x2 = []
    y = []
    for row in inputs:
        x1.append(row[0])
        x2.append(row[1])
        y.append(row[2])

    return pd.DataFrame(list(zip(x1, x2, y)), columns=['x1', 'x2', 'y'])
