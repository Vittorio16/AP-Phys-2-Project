import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

d = 154 * 10**(-6) # slit seperation in m
max_y = 1.4 # wall distance in m
max_x = 1 # viewpoint width in m
point_step = .01 # amount of points between 0 and max
wavelength = 632.8 # in nm
hf = (1.24 * 10**3 / wavelength)


x_positive = d/2 # positive slit position
x_negative = 0 - x_positive # negative slit position

x_list = []
y_list = []
z_list = []
z_list_positive = []
z_list_negative = []
len_positive = []

for y in np.linspace(.2, (max_y + point_step), int(max_y / point_step)):
    for x in np.linspace(-max_x, (max_x + point_step), int((2 * max_x) / point_step)):
        length_positive = np.sqrt(y**2 + (x - x_positive)**2)
        length_negative = np.sqrt(y**2 + (x - x_negative)**2)
        sphere =  1 / (4 * np.pi * length_positive**2)
        z_positive = np.sin(2 * np.pi * length_positive / (wavelength * 10**(-9))) * hf * sphere
        z_negative = np.sin(2 * np.pi * length_negative / (wavelength * 10**(-9))) * hf * sphere
        z = z_positive + z_negative
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        
X, Y, Z = np.array(x_list), np.array(y_list), np.array(z_list)
fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection='3d')

surf = ax.plot_trisurf(X, Y, Z, cmap = plt.cm.cividis)

plt.savefig('foo.png', bbox_inches='tight')