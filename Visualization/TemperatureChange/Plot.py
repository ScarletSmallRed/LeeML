from matplotlib import pyplot as plt
import random

x = range(0, 120, 3)
y1 = [random.randint(20, 35) for i in range(0, 120, 3)]
y2 = [random.randint(20, 35) for i in range(0, 120, 3)]

plt.figure(figsize = (20, 8), dpi = 80)

plt.plot(x, y1, label = 'Room 1')
plt.plot(x, y2, label = 'Room 2')

_x_labels = ['10:{}'.format(i) if i >= 10 else '10:0{}'.format(i) for i in range(60)]
_x_labels += ['11:{}'.format(i) if i >= 10 else '11:0{}'.format(i) for i in range(60)]
plt.xticks(list(x)[::2], _x_labels[::6], rotation = 45)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature Trend From 10:00 to 12:00')
plt.legend()

plt.savefig('./tempearture.png')
plt.show()