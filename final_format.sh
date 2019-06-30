#!/bin/bash

# Create the final file and put a header on it.
echo "Start End" > output.tbl
cat islands.txt >> output.tbl

# Remove intermediate files.
rm *.results
rm start_coordinates.txt end_coordinates.txt start_end.tsv islands.txt
