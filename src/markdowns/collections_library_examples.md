```shell
In [1]: from collections import Counter

In [2]: c = Counter([1, 4, 5, 6, 7, 1, 9 + 1, 90, 10, 0 + 1, 8 - 2, 45 * 2])

In [3]: c
Out[3]: Counter({1: 3, 4: 1, 5: 1, 6: 2, 7: 1, 10: 2, 90: 2})

In [4]: for key, value in c.items():
   ...:     print(key, '->', value)
   ...: 
1 -> 3
4 -> 1
5 -> 1
6 -> 2
7 -> 1
10 -> 2
90 -> 2

In [5]: for key, value in c.items():
   ...:     print(f"{key} -> {value}")
   ...: 
   ...: 
1 -> 3
4 -> 1
5 -> 1
6 -> 2
7 -> 1
10 -> 2
90 -> 2
```