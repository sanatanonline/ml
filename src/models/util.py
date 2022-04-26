import numpy as np


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
