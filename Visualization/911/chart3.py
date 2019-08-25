import pandas as pd
import matplotlib.pyplot as plt

file_path = './911.csv'
df = pd.read_csv(file_path)

df['timeStamp'] = pd.to_datetime(df['timeStamp'], format = '%Y/%m/%d')
df.set_index('timeStamp', inplace = True)
# count_by_month = df.resample('M')
# print(count_by_month)

def split_title(title):
    result = title.split(':')[0]
    return result

df['title'] = df['title'].apply(split_title)
group_title = df.groupby('title')

data = {}
for group_name, group_data in group_title:
    print(group_name)
    print(group_data.resample('M')['e'].count())
    data[group_name] = group_data.resample('M')['e'].count()
    print('*' * 100)

plt.figure(figsize = (20, 8), dpi = 80)
# print(type(data['EMS']))
x = []
for key in data:
    if len(x) == 0:
        x = [i.strftime('%Y-%m') for i in data[key].index]
    plt.plot(x, data[key].values, label = key)

plt.xticks(rotation = 45)
plt.xlabel('Month')
plt.ylabel('Number of Emergence Calls')
plt.legend(loc = 'best')

plt.savefig('./chart3.png')
plt.show()