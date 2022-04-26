import util
import data
import random
import seaborn as sns
import matplotlib.pyplot as plt

random.seed(42)

df = data.load("lc.csv")
p = sns.scatterplot(x=df['x1'], y=df['x2'], hue=df['y'])
p.set_xlabel("X1")
p.set_ylabel("X2")
plt.show()

weights = [0.3, 0.7]
bias = 0.1
iteration = []
output = []

for index, row in df.iterrows():
    net = util.activate(weights, row, bias)
    s = util.logsigmoid(net)
    output.append(s)
    iteration.append(index)

errors = (df["y"] - output)

p = sns.lineplot(x=errors, y=output)
p.set_xlabel("Number of Iterations")
p.set_ylabel("Error")
plt.show()
