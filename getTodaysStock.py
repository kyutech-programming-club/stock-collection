import pandas as pd
import datetime as dt
from datetime import date, timedelta
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt

end = dt.date.today()
start = end - timedelta(days=365)

df = web.DataReader('7203.T', "yahoo", start, end)
df2 = pd.DataFrame({'TOYOTA': df['Close']})

stocks = np.array(df2.values.tolist())
dates = df2.reset_index().values.tolist()
base = 810

for num in range(240):
    if abs(stocks[num] - stocks[num+4]) > base or abs(stocks[num] - stocks[num+3]) > base or abs(stocks[num] - stocks[num+2]) > base or abs(stocks[num] - stocks[num+1]) > base:
        print(dates[num]) 

v = []

for i in range(len(stocks)):
    v.append(stocks[i][0])
# print(v)

df2.plot(title='TOYOTA', grid=True)
plt.show()
