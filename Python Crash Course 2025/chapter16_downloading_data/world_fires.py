# WORLD FIRES = In the resources for this chapter, you’ll find a file 
# called world_fires_1_day.csv. This file contains information about fires 
# burning in different locations around the globe, including the latitude, 
# longitude, and brightness of each fire. Using the data-processing work from
# the first part of this chapter and the mapping work from this section, make 
# a map that shows which parts of the world are affected by fires.

from pathlib import Path
import csv
import plotly.express as px

# Read the CSV file containing wildfire data
path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)  # Skip the header row

# Initialise lists to store data
lats, lons, brights = [], [], []

# Extract relevant data from each row
for row in reader:
    try:
        lat = float(row[0])       # Latitude
        lon = float(row[1])       # Longitude
        bright = float(row[2])    # Brightness
    except ValueError:
        # Print the date (or index) where data is invalid
        print(f"Invalid data for {row[5]}")
    else:
        # Add valid data to the lists
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# Plot data using Plotly
title = "Global wildfire activity"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=brights,                  # Bubble size reflects brightness
    title=title,
    color=brights,                 # Color gradient also reflects brightness
    color_continuous_scale='Viridis',  # Visual scale
    labels={'color': 'Brightness'},
    projection='natural earth',   # Map projection
)

fig.show()  # Show the interactive plot
