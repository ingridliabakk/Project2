
from sklearn import *
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor

class PolyReg:

    poly_reg= None
    features = None
    col_to_predict=None
    def __init__(self, features, train_df, col_to_predict):
        self.col_to_predict = col_to_predict
        y = train_df[col_to_predict]
        self.features = features
        X = train_df[features]
        self.poly_reg = RandomForestRegressor(max_depth=2, random_state=0)
        self.poly_reg.fit(X ,y)


    def R2(self, test_df):
        X = test_df[self.features]
        y = test_df[self.col_to_predict]
        return self.poly_reg.score(X, y)


    def MSE(self, test_df):
        y_true = test_df[self.col_to_predict]
        y_pred = self.poly_reg.predict(test_df[self.features])
        return mean_squared_error(y_true, y_pred)