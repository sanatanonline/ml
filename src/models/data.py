import pandas as pd

ROOT_DIR = "/Users/sanatan/local/code/ml/data/raw/"


def load(filename):
    return pd.read_csv(ROOT_DIR + filename)
