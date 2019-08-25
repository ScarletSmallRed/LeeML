import pandas as pd
import matplotlib.pyplot as plt

file_path = './pm25/BeijingPM20100101_20151231.csv'
df = pd.read_csv(file_path)

periods = pd.PeriodIndex(year = df['year'], month = df['month'], day = df['day'], hour = df['hour'], freq = 'H')
df['date_time'] = periods
df.set_index('date_time', inplace = True)
df = df.resample('7D').mean()
data = df['PM_US Post'].dropna()

x = [i.strftime('%Y-%m-%d') for i in data.index]
y = data.values

plt.figure(figsize = (20, 10), dpi = 80)
plt.plot(x, y)
plt.xticks(x[::15], rotation = 45)
plt.xlabel('Date')
plt.ylabel('PM 2.5')
plt.savefig('./chart.png')
plt.show()