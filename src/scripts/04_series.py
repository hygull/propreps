"""
Description
===========
	This module contains different example and usages of Python Series

Command to run the script
=========================
	python3 ./src/scripts/04_series.py
"""

import pandas as pd


numbers = pd.Series([12, 4, 57, 8, 9, 10])
print(numbers)
"""
O/P
---
0    12
1     4
2    57
3     8
4     9
5    10
dtype: int64
"""

# Vectorized operation
numbers = numbers + 1
print(numbers)
"""
O/P
---
0    13
1     5
2    58
3     9
4    10
5    11
dtype: int64
"""

# Print the first value (By default the values are labeled with the index numbers)
print(numbers[0], numbers[1])
"""
O/P (python3 ./src/scripts/04_series.py)
=========================================
13 5
"""

# With index argument, we can name our own labels
even_numbers = pd.Series(
    [12, 4, 10, 8, 4, 88], index=["pos0", "pos1", "pos2", "pos3", "pos4", "pos5"]
)
print(even_numbers)
"""
O/P
---
pos0    12
pos1     4
pos2    10
pos3     8
pos4     4
pos5    88
dtype: int64
"""

# Items can be accessed by referring to the label
print(even_numbers["pos5"])
"""
O/P
---
88
"""

# Create a simple pandas Series from a dictionary
odd_numbers_map = {"one": 1, "seven": 7, "nine": 9, "eleven": 11, "three": 3, "five": 5}
odd_numbers = pd.Series(odd_numbers_map)
print(odd_numbers)
"""
O/P
---
one        1
seven      7
nine       9
eleven    11
three      3
five       5
dtype: int64
"""

odd_numbers = odd_numbers + 2  # Vectorized operation
print(odd_numbers)
"""
O/P
---
one        3
seven      9
nine      11
eleven    13
three      5
five       7
dtype: int64
"""

# Select only some of the items in a dictionary
mixed_numbers_map = {"one": 1, "two": 2, "twelve": 12, "nineteen": 19, "twenty": 20}
mixed_numbers = pd.Series(mixed_numbers_map, index=["one", "two", "twenty"])
print(mixed_numbers)
"""
O/P
---
one        1
two        2
twenty    20
dtype: int64
"""
