# Import libraries.
import pandas as pd

# Insert the dataset as a csv file.
dataset = pd.read_csv('not_so_raw.results', sep=' ', header=None)

# Create a list to store the starting coordinates of each N-island.
begining_list = [dataset.iloc[0,0]]

# Parse through the csv file and add the starting points of each N-island.
for i in range(len(dataset.iloc[1:, 0])):
    # If a position differs from the one in the other column one row above it,
    # then a new island has started.
    if dataset.iloc[i, 0] != (dataset.iloc[i+1, 0]-1):
        begining_list.append(dataset.iloc[i+1, 0])

start_coordinates = open('start_coordinates.txt', 'w+')

for i in range(len(begining_list)):
    start_coordinates.write(str(begining_list[i]) + '\n')

start_coordinates.close()
