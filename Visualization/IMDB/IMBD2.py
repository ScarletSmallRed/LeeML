import pandas as pd
import matplotlib.pyplot as plt

file_path = './IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)

runtime_data = df['Runtime (Minutes)'].values
print(runtime_data)
print(runtime_data.min(), runtime_data.max())


plt.figure(figsize = (20, 8), dpi = 80)
plt.hist(runtime_data, bins = range(60, 194, 2))
plt.xticks(range(60, 194, 4), rotation = 45)
plt.grid(alpha = 0.5)

plt.xlabel('Movie Runtime (Minutes)')
plt.ylabel('Number of Movies')

plt.savefig('IMBD2.png')
plt.show()