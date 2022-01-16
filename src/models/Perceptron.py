import numpy as np


def activate(weights, inputs, bias):
    activation = 0
    for i in range(len(weights)):
        activation += weights[i] * inputs[i]
    return activation + bias


def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    ds = s * (1 - s)
    return s, ds


def tansigmoid(x):
    t = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    dt = 1 - t ** 2
    return t, dt


def purelinear(x):
    return x


w = [0.2, -0.1, 0.1]
p = [0.4, 0.2, 0.2]
b = 0
net = activate(w, p, b)
print("The net value is:")
print(net)
# for logsigmoid function
a, d_of_a = sigmoid(net)
# for tansigmoid function
# a, d_of_a = tansigmoid(net)
# for linear function
# a = purelinear(net)
print("The output value is:")
print(a)
