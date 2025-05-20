# THREE DICE = When you roll three D6 dice, the smallest number you can roll 
# is 3 and the largest number is 18. Create a visualization that shows what
# happens when you roll three D6 dice.

import plotly.express as px

from dice import Die

# create three D6 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# make some rolls, and store results in a list
results = []
for roll_num in range(30000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    
# analyse the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# visualise the results 
title = "Results of Rolling Three D6s 30000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# further customisations to chart
fig.update_layout(xaxis_dtick=1)

fig.show()