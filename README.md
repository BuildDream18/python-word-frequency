
# Problem Statement:

Detailed below are the key points to the problem that needs solving:

- There is an input file on a Unix system, and it is plain text.

- Each line in the file contains one token (a string of arbitrary chars).

- The input file is extremely large in terms of number of lines.

- The program has as much RAM as needed.

- The program may make one pass only over the data, reading each line just once.

- At the end of the first pass, the program prints a report for each unique token that it found. It should print out the token value itself and the number of times the token was found in the data file.

- Sort order of the output does not matter, but each unique token may appear only once in the output.



# Questions to Address:

- What algorithmic approach would you take and what data structures would be used?

- Why is it the best (fastest) solution?


# Notes:

- This should work on a single machine.

- There is no rhyme or reason to the distribution that governs the characteristics of the string data that you may encounter

- Scalability is important and must be taken into account as part of the solution.


# 3 Approaches

- Standard approach; Reads a large file line by line (for memory efficiency and scalability). Then checks each word against a dictionary and increments the word count if a word is present or adds a new word.
- Efficient approach; As above but uses pre initialized python Collection defaultdict. This removes the use of exceptions for addition / increment and is faster.
- Parallel approach; As the problem lends itself to the mapreduce approach I added a parallel method using python multiprocessing. The large text file is pre split to allow for multi processing. However, this is not an efficient implementation.

# Code
- Tests are made for each approach and are found in "test"
- Tests also have performance benchmarking for timing comparisons.
- I try to write in a functional style with a focus on code readability and clarity.
- Can be run from /examples (see __init__.py)

# Benchmarks
- Stanard approach: 0.4 seconds
- Efficient approach: 0.3 seconds
- Parallel approach: 0.8 seconds

