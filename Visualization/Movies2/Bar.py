import matplotlib.pyplot as plt

movies = ['War for the Planet of the Apes', 'Dunkirk', 'Spider-Man: Homecoming', 'Wolf Warrior 2']
b_14 = [2358, 399, 2358, 362]
b_15 = [12357, 156, 2045, 168]
b_16 = [15746, 312, 4497, 319]

bar_width = 0.2
x_14 = [(i + 1) for i in range(len(movies))]
x_15 = [(i + bar_width) for i in x_14]
x_16 = [(i + bar_width * 2) for i in x_14]

plt.figure(figsize=(20, 8), dpi=80)

plt.bar(x_14, b_14, width=bar_width, label='2019/08/11')
plt.bar(x_15, b_15, width=bar_width, label='2019/08/12')
plt.bar(x_16, b_16, width=bar_width, label='2019/08/13')

plt.xticks(x_15, movies)

plt.title('Three Days Movie Box Office')
plt.xlabel('Movies')
plt.ylabel('Box Office')

plt.legend()

plt.savefig('./Movies.png')
plt.show()

