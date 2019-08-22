import numpy as np

us_file_path = './youtube/USvideos.csv'

t_us = np.loadtxt(us_file_path, delimiter=',', skiprows=1, usecols=7)
print(t_us)