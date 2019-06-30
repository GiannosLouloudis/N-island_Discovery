# # Import libraries.
import pandas as pd
import numpy as np

# Import dataset
dataset = pd.read_csv('start_end.tsv', sep=',', header=None)

# If the difference between the start and end position is less than 100 then drop the row.
for i in range(len(dataset.iloc[:, 0])):
     if dataset.iloc[i, 1] - dataset.iloc[i, 0] < 100:
         dataset.iloc[i, :] = np.nan

data = dataset.dropna()


islands = open('islands.txt', 'w+')

# Insert the start and end positions of the N-islands in the islands.txt file. 
for i in range(len(data.iloc[:,0])):
    islands.write(str(data.iloc[i, 0]) + ' ' + str(data.iloc[i, 1]) + '\n')

islands.close()
