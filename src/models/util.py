import numpy as np


def activate(weights, inputs, bias):
    activation = 0
    for i in range(len(weights)):
        activation += weights[i] * inputs[i]
    return activation + bias


def logsigmoid(x):
    s = 1 / (1 + np.exp(-x))
    ds = s * (1 - s)
    return s, ds


def tansigmoid(x):
    t = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    dt = 1 - t ** 2
    return t, dt


def purelinear(x):
    return x
