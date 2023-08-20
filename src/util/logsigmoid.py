import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from numpy import ndarray


def square(x: ndarray) -> ndarray:
    return np.power(x, 2)


def leaky_relu(x: ndarray) -> ndarray:
    return np.maximum(0.05 * x, x)


def sigmoid(x: ndarray) -> ndarray:
    return 1 / (1 + np.exp(-x))


def tanh(x: ndarray) -> ndarray:
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


fig, ax = plt.subplots(2, 2, sharey=False, figsize=(12, 6))

input_range = np.arange(-1, 1, 0.1)

ax[0, 0].plot(input_range, square(input_range))
ax[0, 0].grid(False, which='both')
ax[0, 0].spines['left'].set_position('zero')
ax[0, 0].spines['right'].set_color('none')
ax[0, 0].yaxis.tick_left()
ax[0, 0].spines['bottom'].set_position('zero')
ax[0, 0].spines['top'].set_color('none')
ax[0, 0].set_title('Square function')
ax[0, 0].set_xlabel('input')
ax[0, 0].set_ylabel('square(x)')

ax[0, 1].plot(input_range, leaky_relu(input_range))
ax[0, 1].grid(False, which='both')
ax[0, 1].spines['left'].set_position('zero')
ax[0, 1].spines['right'].set_color('none')
ax[0, 1].yaxis.tick_left()
ax[0, 1].spines['bottom'].set_position('zero')
ax[0, 1].spines['top'].set_color('none')
ax[0, 1].set_title('Leaky ReLU function')
ax[0, 1].set_xlabel('input')
ax[0, 1].set_ylabel('relu(x)')

ax[1, 0].plot(input_range, sigmoid(input_range))
ax[1, 0].grid(False, which='both')
ax[1, 0].spines['left'].set_position('zero')
ax[1, 0].spines['right'].set_color('none')
ax[1, 0].yaxis.tick_left()
ax[1, 0].spines['bottom'].set_position('zero')
ax[1, 0].spines['top'].set_color('none')
ax[1, 0].set_title('Log sigmoid function')
ax[1, 0].set_xlabel('input')
ax[1, 0].set_ylabel('logsigmoid(x)')

ax[1, 1].plot(input_range, tanh(input_range))
ax[1, 1].grid(False, which='both')
ax[1, 1].spines['left'].set_position('zero')
ax[1, 1].spines['right'].set_color('none')
ax[1, 1].yaxis.tick_left()
ax[1, 1].spines['bottom'].set_position('zero')
ax[1, 1].spines['top'].set_color('none')
ax[1, 1].set_title('Tanh function')
ax[1, 1].set_xlabel('input')
ax[1, 1].set_ylabel('tanh(x)')

plt.show()
