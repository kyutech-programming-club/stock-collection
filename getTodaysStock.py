import pandas as pd
import datetime as dt
from datetime import date, timedelta
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt

end = dt.date.today()
start = end - timedelta(days=365)

df = web.DataReader('7203.T', "yahoo", start, end)
# print(df)
df2 = pd.DataFrame({'TOYOTA': df['Close']})
# print(type(df2))
# print(df2)
s = df2.values.tolist()
Date = df2.reset_index().values.tolist()
print(Date)
# print(s)
# print(len(s))
# print(df['Date'])

v = []

for i in range(len(s)):
    v.append(s[i][0])
# print(v)

df2.plot(title='TOYOTA', grid=True)
plt.show()
