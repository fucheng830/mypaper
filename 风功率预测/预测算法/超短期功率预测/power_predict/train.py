#coding:utf-8

import pandas as pd
import numpy as np
from statsmodels.tsa.api import AR

file_path = './data/zdtmyts_mer.csv'
df = pd.read_csv(file_path)
x = df['real_power']/df['theoryp']
df['x_transfer'] = [l if l>0 else 0 for l in x]
df['y'] = np.log((df['x_transfer']/(pd.Series([1 for i in range(df.shape[0])])-df['x_transfer'])) + pd.Series([1 for i in range(df.shape[0])]))
df.index = pd.DatetimeIndex(df['time'])
#data = df['y']
print df['y']
model = AR(df['y'])
result = model.fit()
#print result.summary()
        