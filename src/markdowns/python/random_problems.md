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

