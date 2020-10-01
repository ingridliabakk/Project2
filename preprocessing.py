import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import datetime
import holidays

def add_datetime(df):
    dates = []
    for index, row in df.iterrows():
        year = row['År']
        month = row['Måned']
        day = row['Dag']

        date = datetime.datetime(year, month, day)
        dates.append(date)
    df['datetime'] = dates


def add_holidays(df):
    nor_holidays = holidays.Norway()
    is_holiday = []
    for index, row in df.iterrows():
        if row['datetime'] in nor_holidays:
            is_holiday.append(True)
            print(row["datetime"])
        else:
            is_holiday.append(False)
    df['is_holiday'] = is_holiday


def add_weekdays(df):
    weekdays = []
    for index, row in df.iterrows():
        datetime = row['datetime']
        day = datetime.weekday()
        weekdays.append(day)
    df['weekdays'] = weekdays