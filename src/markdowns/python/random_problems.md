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