from sklearn import *
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing

class MLP:

    mlp: MLPRegressor = None
    features = None

    def __init__(self, features, train_df, col_to_predict):
        self.col_to_predict = col_to_predict
        y = train_df[col_to_predict]
        self.features = features
        X = train_df[features]
        self.mlp = MLPRegressor(max_iter=200)
        self.mlp.fit(X,y)
        
 
    def test_accuracy(self, test):
        y_true = test[self.col_to_predict]
        y_pred = self.mlp.predict(test[self.features])
        return mean_squared_error(y_true, y_pred)