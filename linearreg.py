from sklearn import *
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import *

class LinearRegression:

    lr: LinearRegression  = None
    features = None

    def __init__(self, features, df, col_to_predict):
        y = df[col_to_predict]
        self.features = features
        X = df[features]
        self.lr = LinearRegression(min_samples_split=20, random_state=99)
        self.lr.fit(X, y)
    
    def test_accuracy(self, test):
        y_true = test["Volum til SNTR"]
        y_pred = self.lr.predict(test[self.features])
        return mean_squared_error(y_true, y_pred)