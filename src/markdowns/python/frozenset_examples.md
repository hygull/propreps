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

In [9]: help(fs1)
```

