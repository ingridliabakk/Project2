from sklearn import *
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.tree import *
import matplotlib.pyplot as plt
class DecisionTree:
    '''
    Class to create a Decision tree and do predictions.
    tree is fitted in the constructor.
    '''
    dt: DecisionTreeRegressor= None
    features = None
    col_to_predict=None
    
    def plot(self,test, col_to_predict):
        '''plot the predicted data and the actual data to compare'''
        y_true = test[col_to_predict]
        y_pred = self.dt.predict(test[self.features])
        plt.plot(y_true, label="actual")
        plt.plot(y_pred, label ="predicted")
        plt.legend()
        plt.show()

    def __init__(self, features, train_df, col_to_predict):
        self.col_to_predict = col_to_predict
        y = train_df[col_to_predict]
        self.features = features
        X = train_df[features]
        self.dt = DecisionTreeRegressor(min_samples_split=20, random_state=99)
        self.dt.fit(X, y)
    
    def R2(self, test_df, col_to_predict = None):
        if col_to_predict is None:
            col_to_predict = self.col_to_predict
        X = test_df[self.features]
        y = test_df[col_to_predict]
        return self.dt.score(X, y)

    def MSE(self, test, col_to_predict = None):
        if col_to_predict is None:
            col_to_predict = self.col_to_predict
        y_true = test[col_to_predict]
        y_pred = self.dt.predict(test[self.features])
        return mean_squared_error(y_true, y_pred)