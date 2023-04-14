import pandas as pd
import re
import matplotlib.pyplot as plt

path = "./data/"
log_filename = path + 'access.log.demo'

#df = pd.read_csv(log_filename, sep=' ', header=None)
#print(df.head(20))
#print(df.iloc[0])

colNames = ('ip', 'dashl', 'userId', 'time', 'url', 'status code', 
            'size of response', 'referer', 'user agent', 'dunno')

df = pd.read_csv(log_filename, sep=' ', header=None, names=colNames)

df.drop(columns=['dashl', 'userId'], inplace=True)


df['time']= df['time'].apply(lambda x: re.search('[\w:/]+', x).group())

#print(df.dtypes)

df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

#newdf = df.loc[(df['time'] > start_date) & (df['time'] < end_date)]
df = df.set_index(['time'])
#newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']

#print(newdf)
downloadSamples = df['size of response'].resample(rule='30Min').mean()
#print(downloadSamples.head(5))


#downloadSamples.plot()
#plt.show()
#print(df.index)
#downloadSamples_1H = df['size of response'].resample(rule='1H')
df_hour_means = df['size of response'].resample(rule='1H').mean()
df_roll_mean6 = df_hour_means.rolling(6).mean()
#print(df_roll_mean6.head(10))
df_roll_mean6.plot()
df_hour_means.plot()

print(df_hour_means.size)
print(df_roll_mean6.size)

plt.legend()
#plt.show()
