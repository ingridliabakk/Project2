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
from linearreg import *
from sklearn.model_selection import train_test_split
plt.style.use('bmh') 
OKGREEN = '\033[92m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def add_features():
    '''adds features and removes unused columns from data'''
    df = (pd.read_csv("data.csv"))
    add_datetime(df)
    add_holidays(df)
    add_weekdays(df)
    add_month(df)
    remove_columns(df)
    return df

def get_features_dataframe():
    '''return a dataframe with engineered features'''
    if(False):
        df = add_features()
        df.to_csv("modifieddata.csv")
    else:
        #read already modified data to save time
        df = pd.read_csv("modifieddata.csv")
    return df

def eval_models(df):
    features = [ 'Fra_time', 'is_holiday', 'weekdays', 'months' ]
    train, test = train_test_split(df, test_size=0.20)
    y_columns = ["Volum til SNTR", "Volum totalt","Volum til DNP"]
    print("mean squared errors")
    for y in y_columns:
        decision_tree = DecisionTree(features, train, y)
        print(f"{OKGREEN} decision tree predicting {y}", decision_tree.test_accuracy(test))
        linreg = LinearRegression(features, train, y)
        print(f"{} decision tree predicting {y}", decision_tree.test_accuracy(test))

if __name__ == "__main__":
    df = get_features_dataframe()
    #plot_features(df)
    print(df.head(100))
    eval_models(df)
