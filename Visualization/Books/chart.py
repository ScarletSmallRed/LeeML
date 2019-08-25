import pandas as pd
import matplotlib.pyplot as plt

file_path = './books.csv'

df = pd.read_csv(file_path)
df.dropna(subset = ['original_publication_year'], inplace = True)
rating_data = df.groupby('original_publication_year')['average_rating'].mean()

_x = rating_data.index
_y = rating_data.values

plt.figure(figsize = (20, 8), dpi = 80)
plt.plot(range(len(_x)), _y)
plt.xticks(range(0, len(_x), 10), _x[::10].astype(int), rotation = 45)
plt.xlabel('Year')
plt.ylabel('Average Rating')

plt.savefig('./chart.png')
plt.show()