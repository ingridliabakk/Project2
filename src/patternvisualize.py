import matplotlib.pyplot as plt
import datetime
import holidays

def plot_features(file):
    df = file
    print(df)
    fig, axs = plt.subplots(3, 2)
    fig.suptitle("Plots")
    
    axs[0][0].title.set_text("Number of cars after first hours")
    axs[0][0].plot(df['Volum totalt'], label='TOT')
    axs[0][0].plot(df['Volum til SNTR'], label='SNTR')
    axs[0][0].plot(df['Volum til DNP'], label='DNP')
    axs[0][0].legend(loc='best')
    
    bars = getholidayavg("Volum til DNP", df) + getholidayavg("Volum til SNTR", df)
    print(bars)
    axs[2][0].bar([1, 2, 3,4], bars )
    axs[2][0].title.set_text("Average/day sorted by holiday and direction")
    axs[2][0].legend(loc='best')
    
    axs[1][0].plot(getweekavg("Volum til SNTR", df), label="SNTR")
    axs[1][0].title.set_text("Total number of cars by weekday")
    axs[1][0].plot(getweekavg("Volum til DNP", df), label="DNP")
    axs[1][0].legend(loc='best')

    # plotting something else
    axs[1][1].plot(getmonthavg("Volum til SNTR", df), label="SNTR")
    axs[1][1].title.set_text("Total number of cars by month")
    axs[1][1].plot(getmonthavg("Volum til DNP", df), label="DNP")
    axs[1][1].legend(loc='best')
    # plotting something else
    axs[2][1].plot(gethouravg("Volum til SNTR", df), label="SNTR")
    axs[2][1].title.set_text("Total number of cars by hour")
    axs[2][1].plot(gethouravg("Volum til DNP", df), label="DNP")
    axs[2][1].legend(loc='best')
    plt.tight_layout()
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