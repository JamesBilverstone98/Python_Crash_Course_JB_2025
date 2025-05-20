# Import necessary libraries
from pathlib import Path  # To handle file paths in an OS-independent way
import csv  # To read data from CSV files
from datetime import datetime  # To convert string dates into datetime objects

import matplotlib.pyplot as plt  # For plotting graphs


def get_weather_data(path, dates, highs, lows, date_index, high_index, low_index):
    """Extract dates, and high/low temperatures from a given CSV file."""
    lines = path.read_text().splitlines()  # Read the CSV file into a list of lines
    reader = csv.reader(lines)  # Create a CSV reader object
    header_row = next(reader)  # Skip the header row (column names)

    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')  # Convert date string to datetime
        try:
            high = int(row[high_index])  # Try to convert high temp to int
            low = int(row[low_index])    # Try to convert low temp to int
        except ValueError:
            # Skip rows where data is missing
            print(f"Missing data for {current_date}")
        else:
            # Append valid data to the lists
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# ------------------- Sitka Weather Data ------------------- #
# Set the path to Sitka CSV file
path = Path('chapter16_downloading_data/sitka_weather_2021_full.csv')
# Create empty lists to store dates and temperatures
dates, highs, lows = [], [], []
# Fill the lists with data from the CSV using column indexes
get_weather_data(path, dates, highs, lows, date_index=2, high_index=4, 
                 low_index=5)

# Start the plot
plt.style.use('seaborn-v0_8')  # Use a cleaner plot style
fig, ax = plt.subplots()  # Create the plot

# Plot Sitka data
ax.plot(dates, highs, color='red', alpha=0.6)  # High temps in red
ax.plot(dates, lows, color='blue', alpha=0.6)  # Low temps in blue
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)# Shaded area between high and low

# ------------------- Death Valley Weather Data ------------------- #
# Reset the lists for Death Valley data
path = Path('chapter16_downloading_data/death_valley_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather_data(path, dates, highs, lows, date_index=2, high_index=3, 
                 low_index=4)

# Plot Death Valley data on the same graph
ax.plot(dates, highs, color='red', alpha=0.3)  # Fainter red line
ax.plot(dates, lows, color='blue', alpha=0.3)  # Fainter blue line
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)  # Lighter shaded area

# ------------------- Format Plot ------------------- #
# Set chart title
title = "Daily high and low temperatures - 2021"
title += "\nSitka, AK and Death Valley, CA"
ax.set_title(title, fontsize=24)

# Label x and y axes
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()  # Format date labels on x-axis for readability
ax.set_ylabel("Temperature (F)", fontsize=16)

# Format tick labels
ax.tick_params(labelsize=16)
ax.set_ylim(10, 140)  # Set temperature range for y-axis

# Display the plot
plt.show()
