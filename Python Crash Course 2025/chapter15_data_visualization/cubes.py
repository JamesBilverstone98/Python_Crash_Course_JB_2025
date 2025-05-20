# CUBES = A number raised to the third power is a cube. Plot the first five 
# cubic numbers, and then plot the first 5,000 cubic numbers.
# Apply a colormap to your cubes plot.

# Importing required libraries
import matplotlib.pyplot as plt  # shortened to plt to save typing
import seaborn as sns  # For enhanced styling options

# Generate data for plotting
x_values = range(1, 5001)           # X-axis: numbers from 1 to 5000
y_values = [x**3 for x in x_values] # Y-axis: each number cubed (x^3)

# Set a visual style
plt.style.use('seaborn-v0_8') # Use a clean Seaborn style for consistency

# Create the figure and axes objects
fig, ax = plt.subplots()  # fig = entire figure; ax = the subplot or chart area

# Create a scatter plot
ax.scatter(
    x_values, y_values,  # The x and y data
    c=y_values,          # Use y-values to determine color intensity
    cmap=plt.cm.Blues,   # Use the 'Blues' colormap for the gradient
    s=10                 # Size of each scatter point
)

# Add chart title and label axes
ax.set_title("Cubic Numbers", fontsize=24)      # Chart title
ax.set_xlabel("Value", fontsize=14)             # Label for the x-axis
ax.set_ylabel("Cube of Value", fontsize=14)     # Label for the y-axis

# Customise tick mark labels (font size)
ax.tick_params(axis='both', labelsize=14)

# Display the plot in a viewer window
plt.show()  



