import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

training_data = pd.read_csv("/Users/sanatan/local/data/titanic/train_data.csv")

nRow, nCol = training_data.shape
print(f'There are {nRow} rows and {nCol} columns')

print(training_data.head(5).to_string())

sns.scatterplot(data=training_data, x="Age", y="Fare", hue="Survived")
plt.show()

