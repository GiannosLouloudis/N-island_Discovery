#!/bin/bash

# Create a two-column table.
awk '{print $3$4}' raw.results > raw.1.tmp
awk -F "=" '{print $2}' raw.1.tmp > raw.2.tmp
sed 's/(//g' raw.2.tmp | sed 's/)//g' | sed 's/,/ /g' > raw.3.tmp

# Create the final table file.
mv raw.3.tmp not_so_raw.results

# Remove temporary files.
rm *.tmp
