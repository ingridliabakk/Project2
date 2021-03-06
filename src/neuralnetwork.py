from sklearn import *
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

class MLP:

    mlp: MLPRegressor = None
    features = None

    def __init__(self, features, train_df, col_to_predict):
        self.col_to_predict = col_to_predict
        y = train_df[col_to_predict]
        self.features = features
        X = train_df[features]
        self.mlp = MLPRegressor(max_iter=50)
        self.mlp.fit(X,y)
        
    def R2(self, test_df):
        X = test_df[self.features]
        y = test_df[self.col_to_predict]
        return self.mlp.score(X, y)
 
    def MSE(self, test):
        y_true = test[self.col_to_predict]
        y_pred = self.mlp.predict(test[self.features])
        return mean_squared_error(y_true, y_pred)