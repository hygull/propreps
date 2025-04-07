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

```python

In [11]: from collections import Counter

In [12]: Counter() == dict()
Out[12]: True

In [13]: Counter() == OrderedDict()
Out[13]: True
```

```python

In [14]: from collections import defaultdict

In [15]: defaultdict() == dict()
Out[15]: True

In [16]: defaultdict() == dict() == Counter()
Out[16]: True

In [17]: defaultdict() == dict() == Counter() == OrderedDict()
Out[17]: True
```