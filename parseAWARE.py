import numpy as np
import sys
import re
from matplotlib import pyplot as plt

fig1 = plt.figure()
plt.hold(True)

data = np.genfromtxt('accelerometer.csv', delimiter=',', dtype='str')

time = np.array(data[:,1], dtype=np.float)
x_acc = data[:,4]
y_acc = data[:,5]
z_acc = data[:,6]

# Normalize to start time, change to [s] 
time = (time - min(time))/1000

plt.plot(time,x_acc, label='X-axis')
plt.plot(time,y_acc, 'r', label='Y-axis')
plt.plot(time,z_acc, 'g', label='Z-axis')
plt.legend()
plt.xlabel('[s]')
plt.ylabel('Magnitude[m/s]')

plt.show()