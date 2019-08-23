import pandas as pd
import matplotlib.pyplot as plt

file_path = './directory.csv'

df = pd.read_csv(file_path)

data = df.groupby('Country')['Brand'].count().sort_values(ascending = False).head(10)

_x = data.index
_y = data.values

plt.figure(figsize = (20, 8), dpi = 80)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x)
plt.xlabel('Country')
plt.ylabel('Number of Starbucks')

plt.savefig('./chart1.png')
plt.show()