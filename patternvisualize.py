import matplotlib.pyplot as plt
import datetime
import holidays

def plot_features(file):
    df = file
    print(df)
    fig, axs = plt.subplots(7)
    fig.suptitle("all plots")
    # axs[0].figure(figsize=(16,8))
    #axs[0].title('Traffic', fontsize = 14)
    #axs[0].xlabel('Timer', fontsize= 12)
    #axs[0].ylabel('Volum Tot', fontsize = 12)
    axs[0].title.set_text("num cars after first hours")
    axs[0].plot(df['Volum totalt'], label='TOT')
    axs[0].plot(df['Volum til SNTR'], label='SNTR')
    axs[0].plot(df['Volum til DNP'], label='DNP')
    axs[0].legend(loc='best')
    # plotting something else
    axs[1].title.set_text("different directions compared")
    axs[1].scatter(df['Volum til SNTR'],
                   df['Volum til DNP'], s=2.5, alpha=0.03)
    #axs[1].axis('equal')
    # plotting something else
    axs[2].title.set_text("volum etter time")
    axs[2].scatter(df['Volum totalt'], df['Fra_time'],
                   cmap='gist_rainbow', s=0.5)
    # plotting something else
    axs[3].title.set_text("volum etter time med begge veier")
    axs[3].scatter(df['Volum til DNP'], df['Fra_time'],
                   cmap='gist_rainbow', s=2.2, c='blue', alpha=0.03)
    axs[3].scatter(df['Volum til SNTR'], df['Fra_time'],
                   cmap='gist_rainbow', s=2.2, c='green', alpha=0.03)
    axs[4].plot(getweekavg("Volum til SNTR", df), label="SNTR")
    axs[4].title.set_text("Total number of cars by weekday")
    axs[4].plot(getweekavg("Volum til DNP", df), label="DNP")
    axs[4].legend(loc='best')
    bars = getholidayavg("Volum til DNP", df) + getholidayavg("Volum til SNTR", df)
    print(bars)
    axs[5].bar([1, 2, 3,4], bars )
    axs[5].title.set_text("Total number of cars by holiday/not holiday, DNP/SNTR")
    axs[5].legend(loc='best')
    # plotting something else
    axs[6].plot(getmonthavg("Volum til SNTR", df), label="SNTR")
    axs[6].title.set_text("Total number of cars by month")
    axs[6].plot(getmonthavg("Volum til DNP", df), label="DNP")
    axs[6].legend(loc='best')
    # plotting something else
    plt.show()

def getholidayavg(col, df):
    hol = [0]*2
    for index, row in df.iterrows():
        day = row['is_holiday']
        if day:
            hol[0] += row[col]
        else:
            hol[1] += row[col]
    return hol

def getweekavg(col, df):
    week = [0]*7
    for index, row in df.iterrows():
        day = row['weekdays']
        week[day] += row[col]
    return week

def getmonthavg(col, df):
    months = [0]*12
    for index, row in df.iterrows():
        month = row['months']
        months[month] += row[col]
    return months