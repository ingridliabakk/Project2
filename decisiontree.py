from sklearn import *
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.tree import *

class DecisionTree:

    dt: DecisionTreeClassifier  = None

    def __init__(self, features, df):
        y = df["Volum til SNTR"]
        X = df[features]
        dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
        dt.fit(X, y)
    
    def test_accuracy(self, test):
        y_true = test["Volum til SNTR"]
        y_pred = self.dt.predict(test["Volum til SNTR"])
        return mean_squared_error(y_true, y_pred)