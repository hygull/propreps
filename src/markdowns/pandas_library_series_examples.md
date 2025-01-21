```python
In [6]: numbers = pd.Series([1, 45, 89, 90, -1, 5.6, 91, 34, -9, -8, 90, 88, 90])

In [7]: numbers
Out[7]: 
0      1.0
1     45.0
2     89.0
3     90.0
4     -1.0
5      5.6
6     91.0
7     34.0
8     -9.0
9     -8.0
10    90.0
11    88.0
12    90.0
dtype: float64

In [8]: for number in numbers:
   ...:     print(number)
   ...: 
1.0
45.0
89.0
90.0
-1.0
5.6
91.0
34.0
-9.0
-8.0
90.0
88.0
90.0

In [9]: numbers_list = [1, 45, 89, 90, -1, 5.6, 91, 34, -9, -8, 90, 88, 90]

In [10]: numbers = pd.Series(numbers_list, index=["INDEX-{i}" for i in range(len(numbers_list))])

In [11]: numbers
Out[11]: 
INDEX-{i}     1.0
INDEX-{i}    45.0
INDEX-{i}    89.0
INDEX-{i}    90.0
INDEX-{i}    -1.0
INDEX-{i}     5.6
INDEX-{i}    91.0
INDEX-{i}    34.0
INDEX-{i}    -9.0
INDEX-{i}    -8.0
INDEX-{i}    90.0
INDEX-{i}    88.0
INDEX-{i}    90.0
dtype: float64

In [12]: numbers = pd.Series(numbers_list, index=[f"INDEX-{i}" for i in range(len(numbers_list))])

In [13]: numbers
Out[13]: 
INDEX-0      1.0
INDEX-1     45.0
INDEX-2     89.0
INDEX-3     90.0
INDEX-4     -1.0
INDEX-5      5.6
INDEX-6     91.0
INDEX-7     34.0
INDEX-8     -9.0
INDEX-9     -8.0
INDEX-10    90.0
INDEX-11    88.0
INDEX-12    90.0
dtype: float64

In [14]: numbers["INDEX-0"]
Out[14]: 1.0

In [15]: numbers[0]
<ipython-input-15-7486ea9d37bc>:1: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
  numbers[0]
Out[15]: 1.0

In [16]: numbers.iloc[0]
Out[16]: 1.0

In [17]: numbers.iloc["INDEX-0"]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[17], line 1
----> 1 numbers.iloc["INDEX-0"]

File ~/Projects/Backend/AiPalette/venvs/topgun_venv3.12.1/lib/python3.12/site-packages/pandas/core/indexing.py:1153, in _LocationIndexer.__getitem__(self, key)
   1150 axis = self.axis or 0
   1152 maybe_callable = com.apply_if_callable(key, self.obj)
-> 1153 return self._getitem_axis(maybe_callable, axis=axis)

File ~/Projects/Backend/AiPalette/venvs/topgun_venv3.12.1/lib/python3.12/site-packages/pandas/core/indexing.py:1711, in _iLocIndexer._getitem_axis(self, key, axis)
   1709 key = item_from_zerodim(key)
   1710 if not is_integer(key):
-> 1711     raise TypeError("Cannot index by location index with a non-integer key")
   1713 # validate the location
   1714 self._validate_integer(key, axis)

TypeError: Cannot index by location index with a non-integer key

In [18]: numbers.loc["INDEX-0"]
Out[18]: 1.0
```