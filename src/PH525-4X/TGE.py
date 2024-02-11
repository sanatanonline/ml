import pandas as pd
import pyreadr

result = pyreadr.read_r("/Users/sanatan/local/data/TGE/tissuesGeneExpression.rda")
print(result.keys())
df1 = result["e"]
df2 = result["tissue"]
df3 = result["tab"]

print(df2.head())
