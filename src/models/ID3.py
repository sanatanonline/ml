from sklearn import tree
from sklearn.preprocessing import LabelEncoder

from src.data import Loader

PlayTennis = Loader.load("PlayTennis.csv")
print(PlayTennis)

y = PlayTennis['play']
X = PlayTennis.drop(['play'], axis=1)

print(X)
print(y)

Le = LabelEncoder()

PlayTennis['outlook'] = Le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp'] = Le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity'] = Le.fit_transform(PlayTennis['humidity'])
PlayTennis['windy'] = Le.fit_transform(PlayTennis['windy'])
PlayTennis['play'] = Le.fit_transform(PlayTennis['play'])

y = PlayTennis['play']
X = PlayTennis.drop(['play'], axis=1)

print(X)
print(y)

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, y)
