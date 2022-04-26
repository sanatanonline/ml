import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [[6.1101, 12.5920], [5.5277, 9.1302], [8.5186, 17.6620], [6.5186, 11.6620], [7.5186, 15.6620]]
df = pd.DataFrame(data, columns=['X', 'Y'])
m = len(df)


def hypothesis(theta_h, x):
    return theta_h[0] + theta_h[1] * x


def cost_calc(theta_x, x, y):
    return (1 / 2 * m) * np.sum((hypothesis(theta_x, x) - y) ** 2)


def gradient_descent(theta_g, x, y, epoch, alpha):
    cost_g = []
    i = 0
    while i < epoch:
        hx = hypothesis(theta_g, x)
        theta_g[0] -= alpha * (sum(hx - y) / m)
        theta_g[1] -= (alpha * np.sum((hx - y) * x)) / m
        cost_g.append(cost_calc(theta_g, x, y))
        i += 1
    return theta_g, cost_g


def predict(theta_p, x, y, epoch, alpha):
    theta_p, cost_p = gradient_descent(theta_p, x, y, epoch, alpha)
    return hypothesis(theta_p, x), cost_p, theta_p


theta = [0, 0]
y_hat, cost, theta = predict(theta, df['X'], df['Y'], 2000, 0.01)

plt.figure()
plt.scatter(df['X'], df['Y'], label='Y')
plt.scatter(df['X'], y_hat, label='Y\u0302')
plt.legend(loc="upper left")
plt.xlabel("Independent variable X")
plt.ylabel("Outcome variable Y")
plt.show()

plt.figure()
plt.scatter(range(0, len(cost)), cost)
plt.show()
