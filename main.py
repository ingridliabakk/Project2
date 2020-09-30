import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')

if __name__ == "__main__":
    file = (pd.read_csv("data.csv"))
    test = file.head(200)
    print(test)
    fig, axs = plt.subplots(4)
    fig.suptitle("all plots")
    #axs[0].figure(figsize=(16,8))
    #axs[0].title('Traffic', fontsize = 14)
    #axs[0].xlabel('Timer', fontsize= 12)
    #axs[0].ylabel('Volum Tot', fontsize = 12)
    axs[0].title.set_text("num cars after first hours")
    axs[0].plot(test['Volum totalt'], label='TOT')
    axs[0].plot(test['Volum til SNTR'], label='SNTR')
    axs[0].plot(test['Volum til DNP'], label='DNP')
    axs[0].legend(loc='best')
    #plotting something else
    axs[1].title.set_text("different directions compared")
    axs[1].scatter(test['Volum til SNTR'], test['Volum til DNP'])
    axs[1].axis('equal')
    #plotting something else
    axs[2].title.set_text("volum etter time")
    axs[2].scatter(test['Volum totalt'], test['Fra_time'])
    #plotting something else
    axs[3].title.set_text("volum etter time")
    axs[3].plot(test['År'], test['Volum totalt'])
    plt.show()
    
    
