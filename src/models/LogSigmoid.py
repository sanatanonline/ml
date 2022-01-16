import numpy as np


def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    ds = s * (1 - s)
    return s, ds


x1 = -0.928
s1, ds1 = sigmoid(x1)
print("------------------------------------------------")
print("The logsigmoid of x1: ", s1)
print("The derivative of logsigmoid of x1: ", ds1)
print("------------------------------------------------")
