import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

slit_sep = 154 # slit seperation in micrometers
d = slit_sep * 10**(-3) # slit sep in mm
max_y = 1400 # wall distance in mm
max_x = 10000 # peaks included 
point_step = 5 # resolution, should be integer
wavelength_input = 632.8 # wavelength in nanometers
λ = wavelength_input * 10**(-6) # wavelength in millimeters
f = 3.00 * (10**8) / (wavelength_input * 10**(-9))
h = 4.135 * 10**(-15)
π = np.pi

x_positive = d/2
x_negative = 0 - x_positive

x_list = []
y_list = []
z_list = []
z_list_positive = []
z_list_negative = []
len_positive = []
for y in np.linspace(0, (max_y + point_step), (max_y / point_step)):
    for x in np.linspace(-max_x, (max_x + point_step), ((2 * max_x) / point_step)):
        length_positive = np.sqrt((y**2) + ((x - x_positive)**2))
        length_negative = np.sqrt((y**2) + ((x - x_negative)**2))
        z_positive = np.sin(2 * π / λ * length_positive) * (h * f / 4 * π * length_positive**2)
        z_negative = np.sin(2 * π / λ * length_negative) * (h * f / 4 * π * length_negative**2)
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

plt.savefig('sin.png', bbox_inches='tight')
