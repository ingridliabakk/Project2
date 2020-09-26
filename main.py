import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')


if __name__ == "__main__":
    file = (pd.read_csv("/Users/ingridingrid/Documents/UiB/H20/INF264/Project2/data.csv"))
    test = file.head(20)

    plt.figure(figsize=(16,8))
    plt.title('Traffic', fontsize = 14)
    plt.xlabel('Timer', fontsize= 12)
    plt.ylabel('Volum Tot', fontsize = 12)
    plt.plot(test['Volum totalt'])
    plt.show()

