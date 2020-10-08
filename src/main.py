import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import datetime
import holidays
from preprocessing import *
from patternvisualize import *
from decisiontree import *
from logreg import *
from linearregresion import *
from neuralnetwork import *
from sklearn.model_selection import train_test_split
plt.style.use('bmh') 
OKGREEN = '\033[92m'
OKBLUE = '\033[94m'
ENDC = '\033[0m'
BOLD = '\033[1m'
ORANGE = '\033[93m'


def add_features():
    '''adds features and removes unused columns from data'''
    df = (pd.read_csv("../data/data.csv"))
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
        df = add_features()
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
    features = [ 'Fra_time', 'is_holiday', 'weekdays', 'months' ]
    train, test = train_test_split(df, test_size=0.20)
    y_columns = ["Volum til SNTR", "Volum totalt","Volum til DNP"]
    print("mean squared errors")
    for y in y_columns:
        decision_tree = DecisionTree(features, train, y)
        print(f"{OKGREEN} decision tree predicting {y}: {decision_tree.test_accuracy(test)}")
        linear_regression = LinRegression(features, train, y)
        print(f"{OKBLUE} linear predicting {y}: {linear_regression.test_accuracy(test)}")
        mlp = MLP(features, train, y)
        print(f"{ORANGE} MLP regressor {y}: {mlp.test_accuracy(test)}")
    print(ENDC)

if __name__ == "__main__":
    df = get_features_dataframe()
    #plot_features(df)
    eval_models(df)
