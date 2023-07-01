import numpy as np

X = [0.5, 2.5]
Y = [0.2, 0.9]


def f(w, b, x):
    return 1.0 / (1.0 + np.exp(-(w * x + b)))


def error(w, b):
    err = 0.0
    for x, y in zip(X, Y):
        fx = f(w, b, x)
        err = err + 0.5 * (fx - y) ** 2
    return err


def gdw(w, b, x, y):
    fx = f(w, b, x)
    return (fx - y) * fx * (1 - fx) * x


def gdb(w, b, x, y):
    fx = f(w, b, x)
    return (fx - y) * fx * (1 - fx)


def run():
    w, b, eta, epochs, = -2, -2, 1.0, 1000
    dw, db = 0.0, 0.0
    for x, y in zip(X, Y):
        dw = dw + gdw(w, b, x, y)
        db = db + gdb(w, b, x, y)
    w = w + eta * dw
    b = b + eta * db
    print("Value of w", w)
    print("Value of b", b)


run()