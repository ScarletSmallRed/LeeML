import pandas as pd
import matplotlib.pyplot as plt

file_path = './911.csv'
df = pd.read_csv(file_path)

df['timeStamp'] = pd.to_datetime(df['timeStamp'], format = '%Y/%m/%d')
df.set_index('timeStamp', inplace = True)

count_by_month = df.resample('M')['e'].count()

_x = [i.strftime('%Y-%m') for i in count_by_month.index]
_y = count_by_month.values

plt.figure(figsize = (20, 8), dpi = 80)
plt.plot(_x, _y)
plt.xticks(rotation = 45)
plt.xlabel('Month')
plt.ylabel('Number of Emergence Calls')

plt.savefig('./chart2.png')
plt.show()