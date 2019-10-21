import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
# print(s)
dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=['a','b','c','d'])
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
# print(df1)

pathBPS = '../rawData/bps.csv'
path_save = '../csv/BPSfilted.csv'
col = ('logtime', 'latitude', 'longitude', 'speed', 'vendorhardwareid')
data = pd.read_csv(pathBPS, usecols=col, chunksize=100000)
i = 0
for chunk in data:
    # print(str(chunk['logtime']).split()[1]+' 01:00:00')
    mask = ((chunk['logtime'] > (str(chunk['logtime']).split()[1]+' 07:00:00')) \
            & (chunk['logtime'] <= (str(chunk['logtime']).split()[1]+' 11:00:00'))) \
            | \
           ((chunk['logtime'] > (str(chunk['logtime']).split()[1] + ' 12:00:00')) \
            & (chunk['logtime'] <= (str(chunk['logtime']).split()[1] + ' 18:00:00')))
    if i == 0:
        chunk.loc[mask].to_csv(path_save, index=False, mode='w')
        i += 1
    else:
        chunk.loc[mask].to_csv(path_save, index=False, header=False, mode='a')
        i += 1
    print(i)
    # filtedData = chunk.loc[(chunk['logtime'][3] == 5), ['logtime', 'latitude', 'longitude', 'speed']]
    # print(chunk[:100])
