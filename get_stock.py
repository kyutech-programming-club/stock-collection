from pandas_datareader import data

df = data.DataReader("7203.T","yahoo")
print(df.iloc['2021-09-11'])