from src.models import data

import seaborn as sns
import matplotlib.pyplot as plt

df = data.load('lc.csv')

sns.scatterplot(data=df, x="x1", y="x2", hue="y")
plt.show()
