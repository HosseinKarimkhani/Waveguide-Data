# Introduction
In this project, the optical field simulation tool spits out a field file in the format:

\# some header stuff

\#   y y y y y y

\# x d d d d d d

\# x d d d d d d

\# x d d d d d d

where y is the y-positions of the grid, x the x-positions and d the E-field data value. Attached with this example are some field files. Assume that the x, y grid distance is not necessarily equidistant, i.e. the distance between adjacent grid lines may vary, denser here, sparser there. Assume in first instance that the field strength on the grid boundary (outer box) is zero.

# What is needed is to regrid/interpolate/extend the field:
- obtain a equidistant grid in x and y.
- add an option to increase the x domain and/or y-domain (set d = 0 outside the original grid), possibly check for d = 0 at the boundary.
- be able to cut out part of the grid smaller than the original field the x-y domain, possibly check if energy is lost when doing that.
- be able to create contour plots of the original and regrided fields.
# Data
Please see the attached files.
# Usage
1: Open First Code File in the Colab.

2: Upload all of the attached files on Colab Files Section.

3: Copy the path's of "hhiE1700.radiusscan.mode.FDteEx_00.txt" from files, and paste it in Line 7, in the provided code.

4: Run the code.

5: Please enter the grid size: This number can be between 1 and 128 (We have 128 data).

6: Please Input your amount of extension in the X-direction here: 10.

7: Please Input your amount of extension in the Y-direction here: 10.

8: Please enter the starting coordinate for the X-axis: 10.

9: Please enter the ending coordinate for the X-axis: 10.

10: Please enter the ending coordinate for the Y-axis: 10.

11: Please enter the ending coordinate for the Y-axis: 10.
