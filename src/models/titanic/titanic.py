import pandas as pd

training_data = pd.read_csv("/Users/sanatan/local/data/titanic/train_data.csv")
nRow, nCol = training_data.shape
print(f'There are {nRow} rows and {nCol} columns')

print(training_data.head(5))