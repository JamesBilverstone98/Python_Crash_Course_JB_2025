# Modify rw_visual.py by replacing ax.scatter() with ax.plot(). 
# To simulate the path of a pollen grain on the surface of a drop of water, 
# pass in the rw.x_values and rw.y_values, and include a linewidth argument.
# Use 5,000 instead of 50,000 points to keep the plot from being too busy.

# Import matplotlib for plotting
import matplotlib.pyplot as plt  # shortened for ease

# Import sys so we can manually add folders to the Python path
import sys
sys.path.append('/Users/jamesmacbook/Desktop/Data Visualisation')
# This line tells Python where to find the file random_walk.py

from random_walk import RandomWalk  # Import the RandomWalk class from the custom module

# Create a RandomWalk instance with 5000 points
rw = RandomWalk(5000)
rw.fill_walk()  # Generate the walk data (x and y values)

# Set a plotting style
plt.style.use('classic')  # Use the classic Matplotlib theme for styling

# Create the figure and axes for plotting
fig, ax = plt.subplots()

# Store the index of each point in the walk
point_numbers = range(rw.num_points)

# Plot the random walk path using a line graph
ax.plot(rw.x_values, rw.y_values, linewidth=3)

# Ensure equal scaling on both axes
ax.set_aspect('equal')

# Highlight the starting point (0,0) in green
ax.scatter(0, 0, c='green', edgecolors='none', s=100)

# Highlight the ending point (last x,y) in red
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Hide the x- and y-axes for a cleaner look
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Display the final plot window
plt.show()

