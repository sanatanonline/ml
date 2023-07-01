import pandas as pd

ROOT_DIR = "/data/raw/"


def load(filename):
    return pd.read_csv(ROOT_DIR + filename)
