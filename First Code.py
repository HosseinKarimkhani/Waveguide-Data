# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MCKPGF2nq8KxHARP8Y3VFCXZllYg-Lvr
"""

############################################################################################
# Step 1: Load data

import numpy as np
import pandas as pd

# Load the data from the file
data = pd.read_csv('/hhiE1700.radiusscan.mode.FDteEx_00.txt', sep="\t", skiprows=4, header=None)

# Separate the x, y, and d values
x = data.iloc[:, 0].values
y = data.iloc[0, :].values
d = data.iloc[1:, 1:].values
x = data.iloc[1:, 0].values  # Drop the first value from 'x'
y = data.iloc[0, 1:].values  # Drop the first value from 'y'


############################################################################################
# Step 2: Interpolate


from scipy.interpolate import griddata

# Convert 1D 'x' and 'y' arrays into 2D arrays
X, Y = np.meshgrid(x, y)

# Flatten the 'X', 'Y', and 'd' arrays
points = np.column_stack((X.flatten(), Y.flatten()))
values = d.flatten()

# Create an equidistant grid
def create_grid(x, y, grid_size):
    grid_x, grid_y = np.mgrid[min(x):max(x):grid_size*1j, min(y):max(y):grid_size*1j]
    return grid_x, grid_y

# Ask the user to input the grid size

while True:
    try:
        grid_size = int(input("Please enter the grid size: "))
        if grid_size > d.shape[0]:
            print(f"The grid size must be less than or equal to {d.shape[0]}. Please try again.")
        else:
            break
    except ValueError:
        print("That's not a valid integer. Please try again.")

# Use the function to create the grid

grid_x, grid_y = create_grid(x, y, grid_size)
# Interpolate the data
grid_d = griddata(points, values, (grid_x, grid_y), method='linear')


############################################################################################
# Step 3: Extension


while True:
    try:
        extension_x = input ('Please Input your amount of extension in the X-direction here: ')
        extension_x = int(extension_x)

        extension_y = input ('Please Input your amount of extension in the Y-direction here: ')
        extension_y = int(extension_y)
        break
    except ValueError:
        print("That's not a valid integer. Please try again.")

# Extend in both the X and Y directions
extended_grid_d = np.zeros((grid_d.shape[0] + 2*extension_y, grid_d.shape[1] + 2*extension_x))

start_index_x = extension_x
end_index_x = start_index_x + grid_d.shape[1]

start_index_y = extension_y
end_index_y = start_index_y + grid_d.shape[0]

extended_grid_d[start_index_y:end_index_y, start_index_x:end_index_x] = grid_d

if np.all(extended_grid_d[0, :] == 0) and np.all(extended_grid_d[-1, :] == 0) and np.all(extended_grid_d[:, 0] == 0) and np.all(extended_grid_d[:, -1] == 0):
    print("d = 0 at all points on the boundary.")
elif np.any(extended_grid_d[0, :] == 0) or np.any(extended_grid_d[-1, :] == 0) or np.any(extended_grid_d[:, 0] == 0) or np.any(extended_grid_d[:, -1] == 0):
    print("d = 0 at some points on the boundary.")
else:
    print("d != 0 at all points on the boundary.")


############################################################################################
# Step 4: Cut

print ('Please provide the starting and ending coordinates for the part of the grid you’re interested in to cut :   ')
while True:
    try:
        start_cut_x = int(input(' Please enter the starting coordinate for the X-axis: '))
        end_cut_x = int(input(' Please enter the ending coordinate for the X-axis: '))
        start_cut_y = int(input(' Please enter the starting coordinate for the Y-axis: '))
        end_cut_y = int(input(' Please enter the ending coordinate for the Y-axis: '))
        break
    except ValueError:
        print("That's not a valid integer. Please try again.")


# Cut out part of the grid
cut_d = d[start_cut_x:end_cut_x, start_cut_y:end_cut_y]


# Calculate total energy before the cut
total_energy_before = np.sum(d**2)

# Calculate total energy after the cut
total_energy_after = np.sum(cut_d**2)

# Check if energy is lost
if total_energy_after < total_energy_before:
    print(" *** Energy is lost when cutting out part of the grid.")
else:
    print(" *** No energy is lost.")

############################################################################################
# Step 5: Plot Original and Regridded Field

import matplotlib.pyplot as plt

# Create a contour plot of the original field
plt.figure()
plt.contourf(x, y, d)
plt.title('Original Field')
plt.colorbar()
plt.show()

# Create a contour plot of the regridded field
plt.figure()
plt.contourf(grid_x, grid_y, grid_d)
plt.title('Regridded Field')
plt.colorbar()
plt.show()

from google.colab import drive
drive.mount('/content/drive')