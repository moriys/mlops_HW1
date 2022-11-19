#!/usr/bin/python3

from sklearn.datasets import load_boston
import pandas as pd
from sklearn.utils import shuffle

boston_dataset = load_boston()
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target
boston = shuffle(boston)

boston.iloc[:400].to_csv("data/raw/train.csv", index=False)
boston.iloc[401:].to_csv("data/raw/test.csv", index=False)

