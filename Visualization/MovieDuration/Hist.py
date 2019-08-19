import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(20, 8), dpi=80)
data = np.random.randint(100, 180, 1000)
plt.hist(data, bins=range(100, 180 + 1,2)) 
plt.xticks(range(100, 180 + 2, 2))
plt.grid(alpha=0.5)
plt.title('1000 Movie Duration Divisions')
plt.xlabel('Movie duration')
plt.ylabel('Number of Movies')
plt.savefig('./MovieDuration.png')
plt.show()