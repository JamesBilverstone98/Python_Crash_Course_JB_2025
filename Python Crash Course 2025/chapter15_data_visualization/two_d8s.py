# TWO D8S = Create a simulation showing what happens when you roll two 
# eight-sided dice 1,000 times. Try to picture what you think the visualization
# will look like before you run the simulation, then see if your intuition was 
# correct. Gradually increase the number of rolls until you start to see the 
# limits of your system’s capabilities.

import plotly.express as px

from die import Die

# create two D8 dice
die_1 = Die(8)
die_2 = Die(8)

# make some rolls, and store results in a list
results = []
for roll_num in range(25000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# analyse the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# visualise the results 
title = "Results of Rolling Two D8s 25000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# further customisations to chart
fig.update_layout(xaxis_dtick=1)

fig.show()