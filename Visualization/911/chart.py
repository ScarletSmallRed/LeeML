import pandas as pd
import matplotlib.pyplot as plt

file_path = './911.csv'
df = pd.read_csv(file_path)

def split_title(title):
    result = title.split(':')[0]
    return result

# print(type(df['title']))
df['title'] = df['title'].apply(split_title)
group_title = df.groupby('title')['e'].count()

_x = group_title.index
_y = group_title.values

plt.figure(figsize = (20, 8), dpi = 80)
plt.bar(_x, _y, width = 0.6)
plt.xlabel('Emergence Type')
plt.ylabel('Number')
plt.savefig('./chart.png')
plt.show()