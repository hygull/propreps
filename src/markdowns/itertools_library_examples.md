```bash
In [1]: import itertools

In [2]: numbers = [1, 3, 5, 6, 8, 10, 15, 11, 12, 13, 2, 7, 9]

In [3]: numbers_islice = itertools.islice(numbers, 5)

In [4]: for tup in numbers_islice:
   ...:     print('tup', tup)
   ...: 
tup 1
tup 3
tup 5
tup 6
tup 8

In [5]: # Loop will not run!

In [6]: for tup in numbers_islice:
    ...:     print('tup', tup)
    ...: 

In [8]: 

In [9]: numbers_islice = itertools.islice(numbers, len(numbers))

In [10]: for tup in numbers_islice:
    ...:     print(tup)
    ...: 
1
3
5
6
8
10
15
11
12
13
2
7
9

In [11]: for tup in numbers_islice:
    ...:     print(tup)
    ...: 

In [12]: 
```

```bash
In [21]: itertools.permutations([1, 2, 3], 2)
Out[21]: <itertools.permutations at 0x7fe239a2efc0>

In [22]: list(itertools.permutations([1, 2, 3], 2))
Out[22]: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

In [23]: list(itertools.combinations([1, 2, 3], 2))
Out[23]: [(1, 2), (1, 3), (2, 3)]

In [24]: list(itertools.permutations([1, 2, 3], 3))
Out[24]: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

In [25]: list(itertools.combinations([1, 2, 3], 3))
Out[25]: [(1, 2, 3)]
```


```bash
In [5]: acc = itertools.accumulate([1, 40, 51, 62, 73, 84, 11, 23, 17])

In [6]: acc
Out[6]: <itertools.accumulate at 0x7fcda800db48>

In [7]: for item in acc:
   ...:     print(item)
   ...: 
1
41
92
154
227
311
322
345
362
```

```bash
In [10]: even_numbers = [2, 80, 4, 46, 8, 16, 10, 12, 100]

In [11]: odd_numbers = [27, 89, 11, 45, 9, 15, 101, 23, 1]

In [12]: mixed_numbers = [99, 45, 68, 22, 31, 90, 67, 1]

In [13]: 

In [13]: chained = itertools.chain(even_numbers, odd_numbers, mixed_numbers)

In [14]: for item in chained:
    ...:     print(item)
    ...: 
2
80
4
46
8
16
10
12
100
27
89
11
45
9
15
101
23
1
99
45
68
22
31
90
67
1

In [15]: 
```


```shell
In [9]: icycle = itertools.cycle([1, 5, 7, 8, 9, 10])

In [10]: count = 0

In [11]: for item in icycle:
    ...:     if count == 20:
    ...:         break
    ...:     print(item)
    ...:     count += 1
    ...: 
1
5
7
8
9
10
1
5
7
8
9
10
1
5
7
8
9
10
1
5
```