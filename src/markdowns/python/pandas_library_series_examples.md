```python
In [5]: import pandas as pd

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
```

```python
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
```

```python
In [18]: numbers.loc["INDEX-0"]
Out[18]: 1.0
```

```python
In [19]: numbers.index
Out[19]: 
Index(['INDEX-0', 'INDEX-1', 'INDEX-2', 'INDEX-3', 'INDEX-4', 'INDEX-5',
       'INDEX-6', 'INDEX-7', 'INDEX-8', 'INDEX-9', 'INDEX-10', 'INDEX-11',
       'INDEX-12'],
      dtype='object')

In [20]: numbers.index.tolist()
Out[20]: 
['INDEX-0',
 'INDEX-1',
 'INDEX-2',
 'INDEX-3',
 'INDEX-4',
 'INDEX-5',
 'INDEX-6',
 'INDEX-7',
 'INDEX-8',
 'INDEX-9',
 'INDEX-10',
 'INDEX-11',
 'INDEX-12']

In [21]: numbers.index = [f"{idx}-X" for idx in numbers.index.tolist()]

In [22]: numbers
Out[22]: 
INDEX-0-X      1.0
INDEX-1-X     45.0
INDEX-2-X     89.0
INDEX-3-X     90.0
INDEX-4-X     -1.0
INDEX-5-X      5.6
INDEX-6-X     91.0
INDEX-7-X     34.0
INDEX-8-X     -9.0
INDEX-9-X     -8.0
INDEX-10-X    90.0
INDEX-11-X    88.0
INDEX-12-X    90.0
dtype: float64
```

```python
In [23]: numbers.sum()
Out[23]: 605.6
```

```python
In [26]: numbers.count()
Out[26]: 13
```

```python
In [30]: numbers.duplicated
Out[30]: 
<bound method Series.duplicated of INDEX-0-X      1.0
INDEX-1-X     45.0
INDEX-2-X     89.0
INDEX-3-X     90.0
INDEX-4-X     -1.0
INDEX-5-X      5.6
INDEX-6-X     91.0
INDEX-7-X     34.0
INDEX-8-X     -9.0
INDEX-9-X     -8.0
INDEX-10-X    90.0
INDEX-11-X    88.0
INDEX-12-X    90.0
dtype: float64>

In [31]: numbers.duplicated()
Out[31]: 
INDEX-0-X     False
INDEX-1-X     False
INDEX-2-X     False
INDEX-3-X     False
INDEX-4-X     False
INDEX-5-X     False
INDEX-6-X     False
INDEX-7-X     False
INDEX-8-X     False
INDEX-9-X     False
INDEX-10-X     True
INDEX-11-X    False
INDEX-12-X     True
dtype: bool

In [32]: numbers[numbers.duplicated()]
Out[32]: 
INDEX-10-X    90.0
INDEX-12-X    90.0
dtype: float64

In [33]: numbers[numbers.duplicated(keep=True)]
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[33], line 1
----> 1 numbers[numbers.duplicated(keep=True)]

File ~/Projects/Backend/AiPalette/venvs/topgun_venv3.12.1/lib/python3.12/site-packages/pandas/core/series.py:2484, in Series.duplicated(self, keep)
   2408 def duplicated(self, keep: DropKeep = "first") -> Series:
   2409     """
   2410     Indicate duplicate Series values.
   2411 
   (...)
   2482     dtype: bool
   2483     """
-> 2484     res = self._duplicated(keep=keep)
   2485     result = self._constructor(res, index=self.index, copy=False)
   2486     return result.__finalize__(self, method="duplicated")

File ~/Projects/Backend/AiPalette/venvs/topgun_venv3.12.1/lib/python3.12/site-packages/pandas/core/base.py:1368, in IndexOpsMixin._duplicated(self, keep)
   1366 @final
   1367 def _duplicated(self, keep: DropKeep = "first") -> npt.NDArray[np.bool_]:
-> 1368     return algorithms.duplicated(self._values, keep=keep)

File ~/Projects/Backend/AiPalette/venvs/topgun_venv3.12.1/lib/python3.12/site-packages/pandas/core/algorithms.py:1011, in duplicated(values, keep)
   1008         return htable.duplicated(values._data, keep=keep, mask=values._mask)
   1010 values = _ensure_data(values)
-> 1011 return htable.duplicated(values, keep=keep)

File pandas/_libs/hashtable_func_helper.pxi:2568, in pandas._libs.hashtable.__pyx_fuse_9duplicated()

File pandas/_libs/hashtable_func_helper.pxi:2591, in pandas._libs.hashtable.duplicated()

File pandas/_libs/hashtable_func_helper.pxi:473, in pandas._libs.hashtable.duplicated_float64()

ValueError: keep must be either "first", "last" or False

In [34]: numbers[numbers.duplicated(keep=False)]
Out[34]: 
INDEX-3-X     90.0
INDEX-10-X    90.0
INDEX-12-X    90.0
dtype: float64

In [35]: numbers[numbers.duplicated(keep='first')]
Out[35]: 
INDEX-10-X    90.0
INDEX-12-X    90.0
dtype: float64

In [36]: numbers[numbers.duplicated(keep='last')]
Out[36]: 
INDEX-3-X     90.0
INDEX-10-X    90.0
dtype: float64

In [37]: numbers.duplicated(keep='first')
Out[37]: 
INDEX-0-X     False
INDEX-1-X     False
INDEX-2-X     False
INDEX-3-X     False
INDEX-4-X     False
INDEX-5-X     False
INDEX-6-X     False
INDEX-7-X     False
INDEX-8-X     False
INDEX-9-X     False
INDEX-10-X     True
INDEX-11-X    False
INDEX-12-X     True
dtype: bool

In [38]: numbers.duplicated(keep='last')
Out[38]: 
INDEX-0-X     False
INDEX-1-X     False
INDEX-2-X     False
INDEX-3-X      True
INDEX-4-X     False
INDEX-5-X     False
INDEX-6-X     False
INDEX-7-X     False
INDEX-8-X     False
INDEX-9-X     False
INDEX-10-X     True
INDEX-11-X    False
INDEX-12-X    False
dtype: bool

In [39]: 
```

```python
In [1]: df =  pd.DataFrame({"even": [12, 0, 22, 56, 80], "odd": [3, 1, 9, 11, 15]})

In [2]: df
Out[2]: 
   even  odd
0    12    3
1     0    1
2    22    9
3    56   11
4    80   15

In [3]: df["even"].nlargest(3)
Out[3]: 
4    80
3    56
2    22
Name: even, dtype: int64

In [4]: df["even"].nlargest(4)
Out[4]: 
4    80
3    56
2    22
0    12
Name: even, dtype: int64

In [5]: df["even"].nlargest(5)
Out[5]: 
4    80
3    56
2    22
0    12
1     0
Name: even, dtype: int64

In [6]: df["even"].nlargest(6)
Out[6]: 
4    80
3    56
2    22
0    12
1     0
Name: even, dtype: int64

In [7]: df["even"].head(3)
Out[7]: 
0    12
1     0
2    22
Name: even, dtype: int64

In [8]: df["even"].head(4)
Out[8]: 
0    12
1     0
2    22
3    56
Name: even, dtype: int64

In [9]: df["even"].head(5)
Out[9]: 
0    12
1     0
2    22
3    56
4    80
Name: even, dtype: int64

In [10]: df["even"].head(6)
Out[10]: 
0    12
1     0
2    22
3    56
4    80
Name: even, dtype: int64
```