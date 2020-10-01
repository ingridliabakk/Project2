import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import datetime
import holidays
from preprocessing import *
plt.style.use('bmh')




def plot_features(file):
    file = (pd.read_csv("data.csv"))
    test = file
    print(test)
    fig, axs = plt.subplots(4)
    fig.suptitle("all plots")
    # axs[0].figure(figsize=(16,8))
    #axs[0].title('Traffic', fontsize = 14)
    #axs[0].xlabel('Timer', fontsize= 12)
    #axs[0].ylabel('Volum Tot', fontsize = 12)
    axs[0].title.set_text("num cars after first hours")
    axs[0].plot(test['Volum totalt'], label='TOT')
    axs[0].plot(test['Volum til SNTR'], label='SNTR')
    axs[0].plot(test['Volum til DNP'], label='DNP')
    axs[0].legend(loc='best')
    # plotting something else
    axs[1].title.set_text("different directions compared")
    axs[1].scatter(test['Volum til SNTR'],
                   test['Volum til DNP'], s=2.5, alpha=0.03)
    axs[1].axis('equal')
    # plotting something else
    axs[2].title.set_text("volum etter time")
    axs[2].scatter(test['Volum totalt'], test['Fra_time'],
                   cmap='gist_rainbow', s=0.5)
    # plotting something else
    axs[3].title.set_text("volum etter time med begge veier")
    axs[3].scatter(test['Volum til DNP'], test['Fra_time'],
                   cmap='gist_rainbow', s=2.2, c='blue', alpha=0.03)
    axs[3].scatter(test['Volum til SNTR'], test['Fra_time'],
                   cmap='gist_rainbow', s=2.2, c='green', alpha=0.03)

    plt.show()


if __name__ == "__main__":
    df = (pd.read_csv("data.csv"))
    add_datetime(df)
    add_holidays(df)
    add_weekdays(df)
    print(df.head(100))
    # plot_features(dataframe)
