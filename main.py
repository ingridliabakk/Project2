import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import datetime
import holidays
from preprocessing import *
from patternvisualize import *
plt.style.use('bmh') 



if __name__ == "__main__":
    df = (pd.read_csv("data.csv"))
    add_datetime(df)
    add_holidays(df)
    add_weekdays(df)
    add_month(df)
    print(df.head(100))
    plot_features(df)




