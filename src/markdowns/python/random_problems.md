```python
In [36]: s = """(1) Rs. 735
    ...: (2) Rs. 1338
    ...: (3) Rs. 632
    ...: (4) Rs. 2085
    ...: (5) Rs. 659
    ...: (6) Rs. 4645
    ...: (7) Rs. 440
    ...: (8) Rs. 830"""

In [37]: lines = s.split("\n")

In [38]: lines
Out[38]: 
['(1) Rs. 735',
 '(2) Rs. 1338',
 '(3) Rs. 632',
 '(4) Rs. 2085',
 '(5) Rs. 659',
 '(6) Rs. 4645',
 '(7) Rs. 440',
 '(8) Rs. 830']

In [39]: prices = [int(line.split()[-1]) for line in lines]

In [40]: prices
Out[40]: [735, 1338, 632, 2085, 659, 4645, 440, 830]

In [41]: sum(prices)
Out[41]: 11364
```


```python
In [1]: a, b, c = 10, 15, 23

In [2]: a
Out[2]: 10

In [3]: b
Out[3]: 15

In [4]: c
Out[4]: 23

In [5]: a2 = 10; b2 = 56; c2 = 89

In [6]: a2
Out[6]: 10

In [7]: b2
Out[7]: 56

In [9]: c2
Out[9]: 89
```

```python
In [1]: numbers = list()

In [2]: numbers.append(12)

In [3]: numbers.append(19)

In [4]: numbers.append(21)

In [5]: numbers
Out[5]: [12, 19, 21]

In [6]: numbers.extend([91, 45, 78, 90])

In [7]: numbers
Out[7]: [12, 19, 21, 91, 45, 78, 90]

In [8]: numbers.pop()
Out[8]: 90

In [9]: numbers
Out[9]: [12, 19, 21, 91, 45, 78]

In [10]: numbers.insert(0, 34)

In [11]: numbers
Out[11]: [34, 12, 19, 21, 91, 45, 78]

In [12]: 
```

```python
In [12]: print("\n".join(["*" * i for i in range(1, 6)]))
*
**
***
****
*****
```

```python
In [1]: (a, b) = 90, 78

In [2]: a
Out[2]: 90

In [3]: b
Out[3]: 78

In [4]: a, b = 56, 45

In [5]: a
Out[5]: 56

In [6]: b
Out[6]: 45

In [7]: [a, b] = 100, 200

In [8]: a
Out[8]: 100

In [9]: b
Out[9]: 200

In [10]: [c, d, e] = [12, 45, 78]

In [11]: c
Out[11]: 12

In [12]: d
Out[12]: 45

In [13]: e
Out[13]: 78
```

```python
In [14]: ((a, b), c) = ((100, 300), 500)

In [15]: a
Out[15]: 100

In [16]: b
Out[16]: 300

In [17]: c
Out[17]: 500
```

```python
In [18]: a, b, c, d = list("ABCD")

In [19]: a
Out[19]: 'A'

In [20]: b
Out[20]: 'B'

In [21]: c
Out[21]: 'C'

In [22]: d
Out[22]: 'D'
```

```python
In [23]: a, b, c, d = list("ABCD")[::-1]

In [24]: d, c, b, a
Out[24]: ('A', 'B', 'C', 'D')

In [25]: d, c, b, a,
Out[25]: ('A', 'B', 'C', 'D')

In [26]: a, b, c, d = list("ABCD")

In [27]: d, c, b, a,
Out[27]: ('D', 'C', 'B', 'A')
```

```python
In [1]: evens = [number for number in [1, 3, 4, 5, 6, 7, 8, 9] if number % 2 == 0]

In [2]: evens
Out[2]: [4, 6, 8]

In [3]: odds = [number for number in [1, 3, 4, 5, 6, 7, 8, 9] if number % 2 != 0]

In [4]: odds
Out[4]: [1, 3, 5, 7, 9]
```

```python
In [5]: {key: value for key, value in zip(["name", "age"], ["Rishikesh Agrawani", 32])}
Out[5]: {'name': 'Rishikesh Agrawani', 'age': 32}
```

```python
In [6]: zip(["name", "age"], ["Rishikesh Agrawani", 32])
Out[6]: <zip at 0x12c0efd80>

In [7]: list(zip(["name", "age"], ["Rishikesh Agrawani", 32]))
Out[7]: [('name', 'Rishikesh Agrawani'), ('age', 32)]

In [8]: for tup in zip(["name", "age"], ["Rishikesh Agrawani", 32]):
   ...:     print(tup)
   ...: 
('name', 'Rishikesh Agrawani')
('age', 32)

In [9]: tuple(zip(["name", "age"], ["Rishikesh Agrawani", 32]))
Out[9]: (('name', 'Rishikesh Agrawani'), ('age', 32))

In [10]: dict(zip(["name", "age"], ["Rishikesh Agrawani", 32]))
Out[10]: {'name': 'Rishikesh Agrawani', 'age': 32}
```

```python
In [11]: zip(["evens", "odds"], zip([2, 5], [4, 9]))
Out[11]: <zip at 0x10ff8a540>

In [12]: list(zip(["evens", "odds"], zip([2, 5], [4, 9])))
Out[12]: [('evens', (2, 4)), ('odds', (5, 9))]

In [13]: dict(zip(["evens", "odds"], zip([2, 5], [4, 9])))
Out[13]: {'evens': (2, 4), 'odds': (5, 9)}

In [14]: tuple(zip(["evens", "odds"], zip([2, 5], [4, 9])))
Out[14]: (('evens', (2, 4)), ('odds', (5, 9)))
```

```python
In [1]: list(dict([("name", 'Rishikesh Agrawani'), ('age', 32)]))
Out[1]: ['name', 'age']

In [2]: dict([("name", 'Rishikesh Agrawani'), ('age', 32)])
Out[2]: {'name': 'Rishikesh Agrawani', 'age': 32}

In [3]: list(dict([("name", 'Rishikesh Agrawani'), ('age', 32)]).keys())
Out[3]: ['name', 'age']

In [4]: list(dict([("name", 'Rishikesh Agrawani'), ('age', 32)]).values())
Out[4]: ['Rishikesh Agrawani', 32]
```

```python
In [40]: _222 = 555

In [41]: print(_222)
555

In [42]: _d1992 = 90

In [43]: print(_d1992)
90

In [44]: _a, _b, _c = 89, 45, 23

In [45]: print(_a, _b, _c)
89 45 23
```

```python
In [38]: (1, 5, 6)
Out[38]: (1, 5, 6)

In [39]: (1, 5, 6) + tuple([11, 45, 67])
Out[39]: (1, 5, 6, 11, 45, 67)

In [40]: (1, 5, 6) + tuple([11, 45, 67, 00])
Out[40]: (1, 5, 6, 11, 45, 67, 0)

In [41]: 0000
Out[41]: 0

In [42]: 000 + 0000 + 0 + 10
Out[42]: 10

In [43]: 000 + 0000 + 0
Out[43]: 0

In [44]: 00 + int('00')
Out[44]: 0

In [45]: 00 + float('00')
Out[45]: 0.0

In [46]: 0.0 + 0000
Out[46]: 0.0
```