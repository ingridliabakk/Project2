import matplotlib.pyplot as plt
import datetime
import holidays

def plot_features(file):
    df = file
    print(df)
    fig, axs = plt.subplots(4, 2)
    fig.suptitle("all plots")
    # axs[0].figure(figsize=(16,8))
    #axs[0].title('Traffic', fontsize = 14)
    #axs[0].xlabel('Timer', fontsize= 12)
    #axs[0].ylabel('Volum Tot', fontsize = 12)
    axs[0][0].title.set_text("num cars after first hours")
    axs[0][0].plot(df['Volum totalt'], label='TOT')
    axs[0][0].plot(df['Volum til SNTR'], label='SNTR')
    axs[0][0].plot(df['Volum til DNP'], label='DNP')
    axs[0][0].legend(loc='best')
    # plotting something else
    axs[1][0].title.set_text("different directions compared")
    axs[1][0].scatter(df['Volum til SNTR'],
                   df['Volum til DNP'], s=2.5, alpha=0.03)
    #axs[1].axis('equal')
    # plotting something else
    axs[2][0].title.set_text("Total cars by hour")
    axs[2][0].scatter(df['Volum totalt'], df['Fra_time'],
                   cmap='gist_rainbow', s=0.5)
    # plotting something else
    axs[3][0].title.set_text("cars in each direction by the hour")
    axs[3][0].scatter(df['Volum til DNP'], df['Fra_time'],
                   cmap='gist_rainbow', s=2.2, c='blue', alpha=0.03)
    axs[3][0].scatter(df['Volum til SNTR'], df['Fra_time'],
                   cmap='gist_rainbow', s=2.2, c='green', alpha=0.03)
    axs[0][1].plot(getweekavg("Volum til SNTR", df), label="SNTR")
    axs[0][1].title.set_text("Total number of cars by weekday")
    axs[0][1].plot(getweekavg("Volum til DNP", df), label="DNP")
    axs[0][1].legend(loc='best')
    bars = getholidayavg("Volum til DNP", df) + getholidayavg("Volum til SNTR", df)
    print(bars)
    axs[1][1].bar([1, 2, 3,4], bars )
    axs[1][1].title.set_text("average/day sorted by holiday and direction")
    axs[1][1].legend(loc='best')
    # plotting something else
    axs[2][1].plot(getmonthavg("Volum til SNTR", df), label="SNTR")
    axs[2][1].title.set_text("Total number of cars by month")
    axs[2][1].plot(getmonthavg("Volum til DNP", df), label="DNP")
    axs[2][1].legend(loc='best')
    # plotting something else
    axs[3][1].plot(gethouravg("Volum til SNTR", df), label="SNTR")
    axs[3][1].title.set_text("Total number of cars by hour")
    axs[3][1].plot(gethouravg("Volum til DNP", df), label="DNP")
    axs[3][1].legend(loc='best')
    plt.show()

def getholidayavg(direction, df):
    hol = [0, 0]
    num_days = [0,0]
    for index, row in df.iterrows():
        day = row['is_holiday']
        if day:
            hol[0] += row[direction]
            num_days[0] += 1
        else:
            hol[1] += row[direction]
            num_days[1] += 1
    hol[0] = hol[0] / num_days[0]
    hol[1] = hol[1] / num_days[1]
    return hol

def gethouravg(col, df):
    week = [0]*24
    for index, row in df.iterrows():
        day = row['Fra_time']
        week[day] += row[col]
    return week

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