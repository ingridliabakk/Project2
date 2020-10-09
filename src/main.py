import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import datetime
import holidays
from preprocessing import *
from polyReg import *
from patternvisualize import *
from decisiontree import *
from randomforest import *
from linearregresion import *
from neuralnetwork import *
from sklearn.model_selection import train_test_split
plt.style.use('bmh') 
OKGREEN = '\033[92m'
OKBLUE = '\033[94m'
ENDC = '\033[0m'
BOLD = '\033[1m'
ORANGE = '\033[93m'

y_columns = ["Volum til SNTR", "Volum totalt","Volum til DNP"]
features = [ 'Fra_time', 'is_holiday', 'weekdays', 'months' ]

def add_features(df):
    '''adds features and removes unused columns from data'''
    add_datetime(df)
    add_holidays(df)
    add_weekdays(df)
    add_month(df)
    remove_columns(df)
    return df

def get_features_dataframe(readFromFile=True):
    '''
    return a dataframe with engineered features. 
    @param readFromFile Reads previously generated features from file
    '''
    if(not readFromFile):
        df = (pd.read_csv("../data/data.csv"))
        df = add_features(df)
        df.to_csv("../data/modifieddata.csv")
    else:
        #read already modified data to save time
        df = pd.read_csv("../data/modifieddata.csv")
    return df

def eval_models(df):
    '''
    Evaluates all models and directions with selected features
    prints MSRP for all models
    '''
    train, test = train_test_split(df, test_size=0.20)
    print("mean squared errors and R2 scores")
    for y in y_columns:
        print("predicting ", y)
        decision_tree = DecisionTree(features, train, y)
        print(f"{OKGREEN} decision tree : {decision_tree.MSE(test):.2f} {decision_tree.R2(test):.2f}", end="")
        linear_regression = PolyReg(features, train, y)
        print(f"{OKBLUE}Random forest: {linear_regression.MSE(test):.0f} {linear_regression.R2(test):.2f}", end="")
        mlp = MLP(features, train, y)
        print(f"{ORANGE} MLP: {mlp.MSE(test):.0f} {mlp.R2(test):.2f}")
        print(ENDC)
    print("predict opposite direction of training data")
    decision_tree = DecisionTree(features, train, 'Volum til SNTR')
    print(f"{BOLD } decision tree : {decision_tree.MSE(test, 'Volum totalt'):.2f} {decision_tree.R2(test, 'Volum til DNP'):.2f}{ENDC}" )

def predict_data(df):
    '''
    try to predict the 2020 data with 2015-2019 data
    prints output and plots prediction and actual value
    '''
    train = df
    test = pd.read_csv("../data/data_2020.csv")
    test = add_features(test)
    print("predicting 2020 data ")
    print("mean squared errors and R2 scores")
    for y in y_columns:
        print("predicting ", y)
        decision_tree = DecisionTree(features, train, y)
        print(f"{OKGREEN} decision tree : {decision_tree.MSE(test):.0f} {decision_tree.R2(test):.2f}", end="")
        print(ENDC)
        decision_tree.plot(test, y)

if __name__ == "__main__":
    df = get_features_dataframe()
    plot_features(df)
    eval_models(df)
    predict_data(df)