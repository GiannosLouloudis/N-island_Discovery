# Import libraries.
import pandas as pd

# Works exactly the same as the startFind.py

#
dataset = pd.read_csv('not_so_raw.results', sep=' ', header=None)

endings_list = []
for i in range(len(dataset.iloc[1:, 0])):
    if dataset.iloc[i, 0] != (dataset.iloc[i+1, 0]-1):
        endings_list.append(dataset.iloc[i, 0]+1)

# Append the last element
endings_list.append(dataset.iloc[-1, 1])

# Create a file to store the end positions.
end_coordinates = open('end_coordinates.txt', 'w+')

for i in range(len(endings_list)):
    end_coordinates.write(str(endings_list[i]) + '\n')

end_coordinates.close()
