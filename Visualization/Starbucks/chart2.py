import pandas as pd
import matplotlib.pyplot as plt

file_path = './directory.csv'

df = pd.read_csv(file_path)
df = df[df['Country'] == 'US']

data = df.groupby('City')['Brand'].count().sort_values(ascending = False).head(25)

_x = data.index
_y = data.values

plt.figure(figsize = (20, 8), dpi = 80)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation = 45)
plt.xlabel('City')
plt.ylabel('Number of Starbucks')

plt.savefig('./chart2.png')
plt.show()