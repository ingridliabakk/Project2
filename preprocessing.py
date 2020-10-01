import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import datetime
import holidays

def add_datetime(df):
    """add datetime object to dataframe"""
    dates = []
    for index, row in df.iterrows():
        year = row['År']
        month = row['Måned']
        day = row['Dag']
        date = datetime.datetime(year, month, day)
        dates.append(date)
    df['datetime'] = dates

def isholiday(timestamp):
    """check if date is a official holiday, høstferie, summer or christmas"""
    nor_holidays = holidays.Norway()
    if timestamp.weekday() in nor_holidays:
        return True
    if timestamp.dt.week in [41, 52, 28, 29, 30]:
        return True
    return False

def add_holidays(df):
    '''adds a true false column describing if date is a holiday'''
    is_holidaylist = []
    for index, row in df.iterrows():
        is_holidaylist.append(isholiday(row['datetime']))
    df['is_holiday'] = is_holidaylist


def add_weekdays(df):
    '''adds weekday numbers 0-6 to dataframe'''
    weekdays = []
    for index, row in df.iterrows():
        datetime = row['datetime']
        day = datetime.weekday()
        weekdays.append(day)
    df['weekdays'] = weekdays