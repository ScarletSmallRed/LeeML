from matplotlib import pyplot as plt
import random

x_mar = range(1, 32)
x_oct = range(51, 82)

temp_mar = [random.randint(20, 30) for i in range(0, 31)]
temp_oct = [random.randint(25, 33) for i in range(0, 31)]

plt.figure(figsize = (20, 8), dpi = 80)

plt.scatter(x_mar, temp_mar, label = 'March')
plt.scatter(x_oct, temp_oct, label = 'October')

_x = list(x_mar) + list(x_oct)
_x_labels = ['03/{}'.format(i) if i >= 10 else '03/0{}'.format(i) for i in range(1, 32)]
_x_labels += ['10/{}'.format(i) if i >= 10 else '10/0{}'.format(i) for i in range(1, 32)]
plt.xticks(_x[::2], _x_labels[::2], rotation = 45)
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()

plt.savefig('./Scatter.png')

plt.show()