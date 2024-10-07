from die import Die
import plotly.express as px

# Create a D6
die = Die()
die2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll() + die2.roll()
    results.append(result)

# print(results)

# Analyze the results
frequencies = []
poss_results = range(2, (die.num_sides * 2) + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# Visualize the results
title = "Results of rolling two D6 1,000 times"
labels = {'x': 'Result','y': 'Frequency of result'}
fig = px.bar(x = poss_results, y= frequencies, title= title, labels= labels)
fig.show()