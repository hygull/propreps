```python
In [1]: [] == ()
Out[1]: False

In [2]: tuple() == ()
Out[2]: True

In [3]: [] == list()
Out[3]: True

In [4]: [] == set()
Out[4]: False

In [5]: set([]) == set()
Out[5]: True

In [6]: dict() == {}
Out[6]: True

In [7]: dict() == dict([])
Out[7]: True
```

```python
In [8]: frozenset() == set()
Out[8]: True
```

```python
In [9]: from collections import OrderedDict

In [10]: OrderedDict() == dict()
Out[10]: True
```