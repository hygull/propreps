```python
In [24]: bool(None) + False
Out[24]: 0

In [25]: bool(None) + False + True
Out[25]: 1

In [26]: bool(None) + False + True + False
Out[26]: 1

In [27]: True + True
Out[27]: 2

In [28]: bool(1)
Out[28]: True

In [29]: bool(0)
Out[29]: False

In [30]: bool("")
Out[30]: False

In [31]: bool([])
Out[31]: False

In [32]: bool(set())
Out[32]: False

In [33]: bool(dict())
Out[33]: False

In [34]: bool(dict(first_name="Rishikesh"))
Out[34]: True

In [35]: set()
Out[35]: set()

In [36]: dict()
Out[36]: {}

In [37]: list()
Out[37]: []

In [38]: dict(list())
Out[38]: {}

In [39]: tuple()
Out[39]: ()
```

```python
In [42]: bool(dict([(1, 12), (4, 7), (5, None)]))
Out[42]: True

In [41]: dict([(1, 12), (4, 7), (5, None)])
Out[41]: {1: 12, 4: 7, 5: None}

In [42]: bool(dict([(1, 12), (4, 7), (5, None)]))
Out[42]: True

In [43]: bool(frozenset())
Out[43]: False

In [44]: bool(1 + 4j)
Out[44]: True

In [45]: bool(0 + 0j)
Out[45]: False

In [46]: bool(1 + 0j)
Out[46]: True

In [47]: bool(0 + 1j)
Out[47]: True
```

```python
In [1]: bool("")
Out[1]: False

In [2]: bool("-")
Out[2]: True

In [3]: bool(1)
Out[3]: True

In [4]: bool(0)
Out[4]: False

In [5]: bool(-1)
Out[5]: True
```

```python
In [7]: bool(10)
Out[7]: True
```

```python
In [8]: bool([1])
Out[8]: True

In [9]: bool([])
Out[9]: False

In [10]: bool(())
Out[10]: False

In [11]: bool(set())
Out[11]: False

In [12]: bool(list())
Out[12]: False

In [13]: bool(tuple())
Out[13]: False
```

```python
In [1]: 1 + int("1")
Out[1]: 2

In [2]: 1 + bool("")
Out[2]: 1

In [3]: 1 + bool("1")
Out[3]: 2

In [4]: 1 + bool("c")
Out[4]: 2

In [5]: 1 + bool("ABC")
Out[5]: 2

In [6]: 1 + bool([])
Out[6]: 1

In [7]: 1 + bool([1, 5])
Out[7]: 2
```