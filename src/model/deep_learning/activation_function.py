from random import seed, gauss

from src.model import util_func
import seaborn as sns
import matplotlib.pyplot as plt

seed(42)
random_numbers = []
for _ in range(10000):
    random_numbers.append(gauss(-1, 1))

linear_values = []
signed_values = []
logsigmoid_numbers = []
tansigmoid_numbers = []
relu_numbers = []
hardtansigmoid_numbers = []

for val in random_numbers:
    linear_values.append(util_func.purelinear(val))
    signed_values.append(util_func.sign(val))
    logsigmoid_numbers.append(util_func.logsigmoid(val))
    tansigmoid_numbers.append(util_func.sign(val))
    relu_numbers.append(util_func.relu(val))
    hardtansigmoid_numbers.append(util_func.hardtansigmoid(val))

plt.subplot(2, 3, 1)
p1 = sns.lineplot(x=random_numbers, y=linear_values)
p1.set_xlabel("x")
p1.set_ylabel("f(x)")
p1.set_title("(i) Linear", y=0, pad=-35, verticalalignment="top")

plt.subplot(2, 3, 2)
p2 = sns.lineplot(x=random_numbers, y=signed_values)
p2.set_xlabel("x")
p2.set_ylabel("f(x)")
p2.set_title("(ii) Sign", y=0, pad=-35, verticalalignment="top")

plt.subplot(2, 3, 3)
p3 = sns.lineplot(x=random_numbers, y=logsigmoid_numbers)
p3.set_xlabel("x")
p3.set_ylabel("f(x)")
p3.set_title("(iii) Sigmoid", y=0, pad=-35, verticalalignment="top")

plt.subplot(2, 3, 4)
p4 = sns.lineplot(x=random_numbers, y=tansigmoid_numbers)
p4.set_xlabel("x")
p4.set_ylabel("f(x)")
p4.set_title("(iv) Tanh", y=0, pad=-35, verticalalignment="top")

plt.subplot(2, 3, 5)
p5 = sns.lineplot(x=random_numbers, y=relu_numbers)
p5.set_xlabel("x")
p5.set_ylabel("f(x)")
p5.set_title("(v) ReLU", y=0, pad=-35, verticalalignment="top")

plt.subplot(2, 3, 6)
p6 = sns.lineplot(x=random_numbers, y=hardtansigmoid_numbers)
p6.set_xlabel("x")
p6.set_ylabel("f(x)")
p6.set_title("(vi) Hard Tanh", y=0, pad=-35, verticalalignment="top")

plt.show()

p = sns.lineplot(x=random_numbers, y=linear_values)
p.set_xlabel("x")
p.set_ylabel("f(x)")
p.set_title("(i) Linear", y=0, pad=-35, verticalalignment="top")
plt.show()

p = sns.lineplot(x=random_numbers, y=signed_values)
p.set_xlabel("x")
p.set_ylabel("f(x)")
p.set_title("(ii) Sign", y=0, pad=-35, verticalalignment="top")
plt.show()

p = sns.lineplot(x=random_numbers, y=logsigmoid_numbers)
p.set_xlabel("x")
p.set_ylabel("f(x)")
p.set_title("(iii) Sigmoid", y=0, pad=-35, verticalalignment="top")
plt.show()

p = sns.lineplot(x=random_numbers, y=tansigmoid_numbers)
p.set_xlabel("x")
p.set_ylabel("f(x)")
p.set_title("(iv) Tanh", y=0, pad=-35, verticalalignment="top")
plt.show()

p = sns.lineplot(x=random_numbers, y=relu_numbers)
p.set_xlabel("x")
p.set_ylabel("f(x)")
p.set_title("(v) ReLU", y=0, pad=-35, verticalalignment="top")
plt.show()

p = sns.lineplot(x=random_numbers, y=hardtansigmoid_numbers)
p.set_xlabel("x")
p.set_ylabel("f(x)")
p.set_title("(vi) Hard Tanh", y=0, pad=-35, verticalalignment="top")
plt.show()
