import pandas as pd


numbers = pd.Series([12, 4, 57, 8, 9, 10])
print(numbers)
"""
O/P (python3 ./src/practice/04_series.py)
=========================================
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
O/P (python3 ./src/practice/04_series.py)
=========================================
0    13
1     5
2    58
3     9
4    10
5    11
dtype: int64
"""
