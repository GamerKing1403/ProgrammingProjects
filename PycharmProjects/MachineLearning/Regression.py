# import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression

# Authentication Process
quandl.ApiConfig.api_key = "vpx9hUHjYztDCPxJy1oY"
# Getting the data from Quandl
df = quandl.get('WIKI/GOOGL')   # Quandl gives A dataframe as a result and df also stands for dataframe
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0  # Percentage of High - low
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0   # Change in percent over the day
df = df[['Adj. Close', 'HL_PCT', 'PCT_Change', 'Adj. Volume']]  # Chooses all the columns needed and ignores the rest
# Close is the feature and the rest are label
forecast_col = 'Adj. Close'     # The column which is being forecasted
df.fillna(-99999, inplace=True)     # Replaces the na with -99999 so that we don't lose data

forecast_out = int(math.ceil(0.01*len(df)))  # We are getting the number of days old forecast to use to predict it

df['label'] = df[forecast_col].shift(-forecast_out)     # Creates labels and shifts it some days up
df.dropna(inplace=True)

x = np.array(df.drop(['label'], 1))     # All the Features are generally used in x
y = np.array(df['label'])   # All the labels are generally used as y

x = preprocessing.scale(x)  # It helps but at the cost of processing time skip if time is of essence

x = x[:-forecast_out+1]
df.dropna(inplace=True)
print(len(x),len(y))