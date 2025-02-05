```python
In [1]: fixed_coordinates = set([frozenset([3, 1]), frozenset([2, 1])])

In [2]: fixed_coordinates
Out[2]: {frozenset({1, 3}), frozenset({1, 2})}

In [3]: for fixed_coordinate in fixed_coordinates:
   ...:     print(fixed_coordinate)
   ...: 
frozenset({1, 3})
frozenset({1, 2})

In [4]: fs1 = frozenset([3, 1])

In [5]: s1 = set([3, 1])

In [6]: s1.add(2)

In [7]: s1
Out[7]: {1, 2, 3}

In [8]: fs1.add(2)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[8], line 1
----> 1 fs1.add(2)

AttributeError: 'frozenset' object has no attribute 'add'
```

```python
In [12]: s1
Out[12]: {1, 2, 3}

In [13]: s2 = {8, 9, 3}

In [14]: s3 = set([1, 4, 6, 2, 8, 3, 1])

In [15]: s2
Out[15]: {3, 8, 9}

In [16]: s3
Out[16]: {1, 2, 3, 4, 6, 8}

In [17]: s1 & s2
Out[17]: {3}

In [18]: s1 & s3
Out[18]: {1, 2, 3}

In [19]: s2 & s3
Out[19]: {3, 8}

In [20]: s1 - s3
Out[20]: set()

In [21]: s2 - s3
Out[21]: {9}

In [22]: s3 - s2
Out[22]: {1, 2, 4, 6}

In [23]: s1 | s3
Out[23]: {1, 2, 3, 4, 6, 8}

In [24]: s1.union(s3)
Out[24]: {1, 2, 3, 4, 6, 8}

In [25]: s1 - s3
Out[25]: set()

In [26]: s1 - s2
Out[26]: {1, 2}

In [27]: s1.difference(s2)
Out[27]: {1, 2}

In [28]: s1 ^ s2
Out[28]: {1, 2, 8, 9}

In [29]: s1.symmetric_difference(s2)
Out[29]: {1, 2, 8, 9}
```