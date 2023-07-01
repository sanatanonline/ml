import numpy as np


def tanh(x):
    t = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    dt = 1 - t ** 2
    return t, dt


x1 = -0.928
t1, dt1 = tanh(x1)
print("------------------------------------------------")
print("The tansigmoid of x1: ", t1)
print("The derivative of tansigmoid of x1: ", dt1)
print("------------------------------------------------")
