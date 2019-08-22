import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = './IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
temp_list = df['Genre'].str.split(',').tolist()
genre_list = list(set([genre for item in temp_list for genre in item]))
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns = genre_list)

for i in range(df.shape[0]):
    zeros_df.loc[i, temp_list[i]] = 1

genre_count = zeros_df.sum(axis = 0).sort_values()
_x = genre_count.index
_y = genre_count.values

plt.figure(figsize = (20, 8), dpi = 80)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation = 45)
plt.xlabel('Movie Type')
plt.ylabel('Number of Movies')
plt.title('Movie Distribution Map of IMDB\'s One Thousand Movie List')
plt.savefig('./IMDB1.png')
plt.show()