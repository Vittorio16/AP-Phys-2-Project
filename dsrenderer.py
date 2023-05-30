import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

print("Calculating units...")
slit_sep = 154 # slit seperation in micrometers
d = slit_sep * 10**(-6) # slit sep (meters)

max_y = 1.4 # wall distance (meters)
max_x = 10 # amount of wall shown on one side from the center (meters)

point_step_unconverted = 5 # resolution in millimeters
point_step = point_step_unconverted * 10**(-3) # resolution (meters)

wavelength_input = 632.8 # wavelength in nanometers
λ = wavelength_input * 10**(-6) # wavelength (meters)

f = 3.00 * (10**8) / λ # frequency
h = 6.63 * 10**(-34) # planck's constant (joule-seconds)
π = np.pi # pi value

x_positive = d/2
x_negative = 0 - x_positive

print("Plotting points...")
x_list = []
y_list = []
z_list = []
z_list_positive = []
z_list_negative = []
len_positive = []
for y in np.linspace(0, (max_y + point_step), int(max_y / point_step)):
    for x in np.linspace(-max_x, (max_x + point_step), int((2 * max_x) / point_step)):
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

print("Converting to graphing arrays...")        
X, Y, Z = np.array(x_list), np.array(y_list), np.array(z_list)
Z_neg, Z_pos = np.array(z_list_negative), np.array(z_list_positive)

print("Graphing...")
fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection='3d')
surf = ax.plot_trisurf(X, Y, Z, cmap = plt.cm.cividis)

print("Converting to image...")
plt.savefig('sin.png', bbox_inches='tight')
print("DONE")
