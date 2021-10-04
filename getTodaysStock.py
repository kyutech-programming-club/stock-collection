import pandas as pd
import datetime as dt
from datetime import date, timedelta
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt

def searchDates():
    end = dt.date.today()
    start = end - timedelta(days=365)

    df = web.DataReader('7203.T', "yahoo", start, end)
    df2 = pd.DataFrame({'TOYOTA': df['Close']})

    stocks = np.array(df2.values.tolist())
    dates = df2.reset_index().values.tolist()

    sum = 0
    base = 0
    print(df)
    for num in range(230):
        sum += stocks[num]
        average = sum / 230
        base = average * 0.08

    for num in range(230):
        if abs(stocks[num] - stocks[num+4]) > base or abs(stocks[num] - stocks[num+3]) > base or abs(stocks[num] - stocks[num+2]) > base or abs(stocks[num] - stocks[num+1]) > base:
            dateData = dates[num][0].strftime('%Y年%m月%d日') 
            dateList = []
            dateList.append(dateData)
            print(dateData)
        
# v = []

# for i in range(len(stocks)):
#     v.append(stocks[i][0])
# # print(v)

# df2.plot(title='TOYOTA', grid=True)
# plt.show()
