# runs_AI_experiment
Experimenting with AI.

Using an AI assistant to generate an interesting piece of code.

The code in this repository, originally generated with the help of a VSCode plugin from Codeium,

* creates a list of random floats [0, 1) of length N
* generates all N! permutations of that list
* decomposes each permutation into contiguous runs, where the first element of each run is the smallest, storing the decomposition as a list of lists.
* counts the number of runs in each permutation
* verifies that these counts correspond to the Sterling numbers of the first kind
