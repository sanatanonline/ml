import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import missingno as msno
from datetime import date
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import RobustScaler, LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve, classification_report, \
    precision_recall_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

import warnings

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df_ = pd.read_csv("/Users/sanatan/local/data/diabetes/pima/diabetes.csv")
df = df_.copy()


def check_df(dataframe, head=10):
    print('\033[1m' + 10 * "*" + ' SHAPE ' + 10 * "*" + '\033[0m')
    print(f"Rows:{dataframe.shape[0]}")
    print(f"Columns:{dataframe.shape[1]}")
    print('\033[1m' + 10 * "*" + ' TYPES ' + 10 * "*" + '\033[0m')
    print(dataframe.dtypes)
    print('\033[1m' + 10 * "*" + ' NUNIQUE ELEMENTS ' + 10 * "*" + '\033[0m')
    print(dataframe.nunique())
    print('\033[1m' + 10 * "*" + ' NA ' + 10 * "*" + '\033[0m')
    print(dataframe.isnull().sum())
    print('\033[1m' + 10 * "*" + ' DESCRIBE ' + 10 * "*" + '\033[0m')
    print(dataframe.describe().T)
    print('\033[1m' + 10 * "*" + ' DUPLICATED VALUE ' + 10 * "*" + '\033[0m')
    print(dataframe.duplicated().sum())
    print('\033[1m' + 10 * "*" + ' HEAD ' + 10 * "*" + '\033[0m')
    print(dataframe.head(head))


check_df(df, 10)

f, ax = plt.subplots(1, 2, figsize=(18, 8))
df['Outcome'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('target')
ax[0].set_ylabel('')
sns.countplot('Outcome', data=df, ax=ax[1])
ax[1].set_title('Outcome')
plt.show()
