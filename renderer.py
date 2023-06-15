import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import re

# Checks if user input is empty
float_pattern = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'
def check_if_valid(elements):
    for element in elements:
        if element == "" or (not re.match(float_pattern, element) and not element.isnumeric()):
            return False
    return True

def create_graph(d, max_y, max_x, point_step, wavelength):
    # d = 154 * 10**(-6) # slit seperation in m
    # max_y = 1.4 # wall distance in m
    # max_x = 1 # viewpoint width in m
    # point_step = .01 # amount of points between 0 and max
    # wavelength = 632.8 # in nm
    d = float(d) 
    max_y = float(max_y) 
    max_x = float(max_x)
    point_step = float(point_step)
    wavelength = float(wavelength)

    x_positive = (max_x/2) + (d/2) # positive slit position
    x_negative = (max_x/2) - (d/2) # negative slit position

    x_list = []
    y_list = []
    z_list = []
    z_list_positive = []
    z_list_negative = []
    len_positive = []

    for y in np.linspace(max_y/10, (max_y + point_step), int(max_y / point_step)):
        for x in np.linspace(0, (max_x + point_step), int(max_x / point_step)):
            length_positive = np.sqrt(y**2 + (x - x_positive)**2)
            length_negative = np.sqrt(y**2 + (x - x_negative)**2)
            z_positive = np.sin(2 * np.pi * length_positive / (wavelength * 10**-9)) * (1240 / wavelength) / (4 * np.pi * length_positive**2)
            z_negative = np.sin(2 * np.pi * length_positive / (wavelength * 10**-9)) * (1240 / wavelength) / (4 * np.pi * length_negative**2)
            z = z_positive + z_negative
            x_list.append(x)
            y_list.append(y)
            z_list.append(z)
            
    X, Y, Z = np.array(x_list), np.array(y_list), np.array(z_list)
    fig = plt.figure(figsize = (12,10))
    ax = plt.axes(projection='3d')
    surf = ax.plot_trisurf(X, Y, Z, cmap = plt.cm.cividis)

    ax.set_xlabel('Position on Wall (meters)')
    ax.set_ylabel('Distance to Wall (meters)')
    ax.set_zlabel('Intensity of Light')

    plt.savefig('static/doubleSlitGraph.png')

create_graph(0.000154, 1.4, 2, 0.01, 632.8)