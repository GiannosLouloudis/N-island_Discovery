# Import libraries.
import re

# Open and read the fasta file.
data = open('chrUN.fasta', "r")
dat = data.read()

# Remove the header and create a list of the lines.
subset = dat[85:1000000].splitlines()

# Creat an empty string called "seq".
seq = ''

# Append every element in the list to the empty string-variable.
for i in range(len(subset)):
    seq += subset[i]

# Use re to define the pattern and apply finditer to the seq.
pattern = re.compile(r'N')
matches = pattern.finditer(seq)

# Append all the hits to a list.
output = []
for match in matches:
    output.append(match)

data.close()

# Create a file of all the hits.
output_file = open('raw.results', 'w+')
for element in range(len(output)):
    output_file.write(str(output[element])+'\n')
output_file.close()
