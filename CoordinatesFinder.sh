#!/bin/bash

# Save the chromosome name to append it later.
chr_name=$(grep "$2" $1)

# Delete all the lines including the Chromosome HG916851.1 and output them in a new file.
sed "1,/$2/d" $1 > no_header_file.txt

# Append the chromosome header to the no_header_file and create the final fasta file.
echo $chr_name > chrUN.fasta
cat no_header_file.txt >> chrUN.fasta

# Remove excessive files.
rm no_header_file.txt

# Find the position of EVERY N-element in the chromosome.
python3 reFind.py
echo "Phase 1: Found N-character coordinates."

# Format the file created above, so that it can be inserted properly in the next script.
./rawProcessing.sh

# Find starting and ending positions of each N-island in the chromosome.
python3 startFind.py
python3 endFind.py

echo "Phase 2: Found starting and ending positions for each island."

# Create a two-column file to with both starting and ending positions.
./concatenator.sh

# Keep only islands consisting of 100 N repeats or more.
python3 islandFind.py
echo "Phase 3: Kept only islands of proper length."

# Create the final table file.
./final_format.sh
echo "Run completed! Do you feel lucky punk?"
