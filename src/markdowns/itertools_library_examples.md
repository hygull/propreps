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