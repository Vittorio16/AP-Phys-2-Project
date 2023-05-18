import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

d = 5 # slit seperation
max_y = 100 # wall distance
max_x = 100 # peaks included
point_step = 0.1 # amount of points between 0 and max
wavelength = 5

x_positive = d/2
x_negative = 0 - x_positive

x_list = []
y_list = []
z_list = []
z_list_positive = []
z_list_negative = []
len_positive = []
for y in np.arange(0, max_y, point_step):
    for x in np.arange(-max_x, max_x, point_step):
        length_positive = np.sqrt((y**2) + ((x - x_positive)**2))
        length_negative = np.sqrt((y**2) + ((x - x_negative)**2))
        z_positive = np.sin(((2 * np.pi) / wavelength) * length_positive)
        z_negative = np.sin(((2 * np.pi) / wavelength) * length_negative)
        z = z_positive + z_negative
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        z_list_positive.append(z_positive)
        z_list_negative.append(z_negative)
        
X, Y, Z = np.array(x_list), np.array(y_list), np.array(z_list)
Z_neg, Z_pos = np.array(z_list_negative), np.array(z_list_positive)

fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection='3d')

surf = ax.plot_trisurf(X, Y, Z, cmap = plt.cm.cividis)

plt.savefig('foo.png', bbox_inches='tight')