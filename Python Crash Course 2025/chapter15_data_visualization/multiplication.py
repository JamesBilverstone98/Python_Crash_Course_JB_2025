# MULTIPLICATION = When you roll two dice, you usually add the two numbers 
# together to get the result. Create a visualization that shows what happens 
# if you multiply these numbers by each other instead

import plotly.express as px

from dice import Die

# create two D6 dice
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list
results = []
for roll_num in range(25000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
    
# analyse the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# visualise the results 
title = "Results of Rolling Two D6s 25000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# further customisations to chart
fig.update_layout(xaxis_dtick=1)

fig.show()