import numpy as np
import pandas as pd
from scipy.spatial.distance import squareform, pdist

a = np.array([1, 2, 2, 1])
b = np.array([1, 1, 2, 2])
point = ['P1', 'P2', 'P3', 'P4']
data = pd.DataFrame({'Point': point, 'a': np.round(a, 2), 'b': np.round(b, 2)})
data = data.set_index('Point')
print(data)

dist = pd.DataFrame(squareform(pdist(data[['a', 'b']]), 'euclidean'), columns=data.index.values,
                    index=data.index.values)
print("----euclidean----")
print(dist)

dist1 = pd.DataFrame(squareform(pdist(data[['a', 'b']], 'cityblock')), columns=data.index.values,
                     index=data.index.values)
print("----manhattan----")
print(dist1)
