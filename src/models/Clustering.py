import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from scipy.spatial.distance import squareform, pdist

a = np.array([1, -1, 2, 3, 0])
b = np.array([1, -1, 2, 3, 0])
point = ['P1', 'P2', 'P3', 'P4', 'P5']
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

plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.title("Dendrogram with Single linkage")
dend = shc.dendrogram(shc.linkage(data[['a', 'b']], method='single', metric='cityblock'), labels=data.index)
plt.show()

plt.subplot(2, 2, 2)
plt.title("Dendrogram with Complete/Maximum linkage")
dend = shc.dendrogram(shc.linkage(data[['a', 'b']], method='complete'), labels=data.index)
plt.show()

plt.subplot(2, 2, 3)
plt.title("Dendrogram with Average linkage")
dend = shc.dendrogram(shc.linkage(data[['a', 'b']], method='average'), labels=data.index)
plt.show()
