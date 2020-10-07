from sklearn import *
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

class LinRegression:

    lr: LinearRegression = None
    features = None

    def __init__(self, features, train_df, col_to_predict):
        self.col_to_predict = col_to_predict
        y = train_df[col_to_predict]
        self.features = features
        X = train_df[features]
        
        #X_scaled = preprocessing.scale(X)
        #y_scaled = preprocessing.scale(y)
        
        self.lr = LinearRegression()
        self.lr.fit(X,y)
        
 
    def test_accuracy(self, test):
        y_true = test[self.col_to_predict]
        y_pred = self.lr.predict(test[self.features])
        return mean_squared_error(y_true, y_pred)