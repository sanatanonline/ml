import random
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from src.models.util import data, util

random.seed(42)

df = data.load("lc.csv")

p = sns.scatterplot(x=df['x1'], y=df['x2'], hue=df['y'])
p.set_xlabel("x1")
p.set_ylabel("x2")
p.set_title("Data Distribution", y=0, pad=-40, verticalalignment="top")
plt.show()

weights = [0.3, 0.7]
bias = 0.1
alpha = 0.5
number_of_epochs = 100
epochs = []
epoch_errors = []

for epoch in range(number_of_epochs):
    errors = []
    for index, row in df.iterrows():
        x = [row['x1'], row['x2']]
        net = util.activate(weights, x, bias)
        s = util.logsigmoid(net)
        if s > row['y']:
            weights = weights + np.multiply(x, alpha)
        else:
            weights = weights - np.multiply(x, alpha)
        errors.append(row['y'] - s)
    epochs.append(epoch)
    epoch_errors.append(np.mean(errors))

p = sns.lineplot(x=epochs, y=epoch_errors)
p.set_xlabel("Number of Epochs")
p.set_ylabel("Training Error")
p.set_title("Average training error decreases with each epoch", y=0, pad=-40, verticalalignment="top")
plt.show()
