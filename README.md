# N-island_Discovery
Parse through an assembled chromosome and identify the coordinates of N-islands greater than 100-N long.

This is a pipeline consisting of 4 Python and 4 Bash scripts.

N-islands are sequences of 100 consecutive Ns that are used to separate sequences of regular bases. Sometimes they can be longer indicating different reasons for their existence.

Manual:
1. Create a directory and place the 8 scripts in it.
2. Move your assembly file (only fasta format) in the directory.
3. Run the CoordinatesFinder.sh script as follows.

./CoordinatesFinder.sh <Assembly_file.fasta> <Chromosome_Name>

Outputs:
- A fasta file that contains the chromosome header and sequence. (chrUN.fasta)
- A two-column table with the coordinates of every startings and ending positions of the N-islands. (output.tbl)
