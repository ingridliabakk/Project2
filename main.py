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
from sklearn.model_selection import train_test_split
plt.style.use('bmh') 

if __name__ == "__main__":
    df = (pd.read_csv("data.csv"))
    add_datetime(df)
    add_holidays(df)
    add_weekdays(df)
    add_month(df)
    remove_columns(df)

    train, test = train_test_split(df, test_size=0.20)
    #plot_features(df)
    print(df.head(100))
    features = [ 'Fra_time', 'is_holiday', 'weekdays', 'months' ]
    decision_tree = DecisionTree(features, train)
    print("dt error", decision_tree.test_accuracy())



