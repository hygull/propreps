```python
In [14]: odd_numbers
Out[14]: {1, 5, 7, 9, 45, 99, 121}

In [15]: even_numbers
Out[15]: {4, 6, 8, 12, 26, 34, 42, 64, 90, 200}

In [16]: 

In [16]: odd_numbers & even_numbers
Out[16]: set()

In [17]: odd_numbers - even_numbers
Out[17]: {1, 5, 7, 9, 45, 99, 121}

In [18]: even_numbers - odd_numbers
Out[18]: {4, 6, 8, 12, 26, 34, 42, 64, 90, 200}

In [19]: numbers = even_numbers | odd_numbers

In [20]: numbers
Out[20]: {1, 4, 5, 6, 7, 8, 9, 12, 26, 34, 42, 45, 64, 90, 99, 121, 200}

In [21]: numbers & even_numbers
Out[21]: {4, 6, 8, 12, 26, 34, 42, 64, 90, 200}

In [22]: numbers & odd_numbers
Out[22]: {1, 5, 7, 9, 45, 99, 121}

In [23]: numbers - even_numbers
Out[23]: {1, 5, 7, 9, 45, 99, 121}

In [24]: numbers - odd_numbers
Out[24]: {4, 6, 8, 12, 26, 34, 42, 64, 90, 200}
```

```python
In [1]: numbers = set([1, 4, 6, 8, 12, 90, 45, 23, 21, 24., 9, 10])

In [2]: numbers
Out[2]: {1, 4, 6, 8, 9, 10, 12, 21, 23, 24.0, 45, 90}

In [3]: numbers.discard(1)

In [4]: numbers
Out[4]: {4, 6, 8, 9, 10, 12, 21, 23, 24.0, 45, 90}

In [5]: numbers.discard(24)

In [6]: numbers
Out[6]: {4, 6, 8, 9, 10, 12, 21, 23, 45, 90}

In [7]: numbers.discard(9)

In [8]: numbers
Out[8]: {4, 6, 8, 10, 12, 21, 23, 45, 90}

In [9]: numbers.discard(3)

In [10]: numbers
Out[10]: {4, 6, 8, 10, 12, 21, 23, 45, 90}

In [11]: numbers.discard(1000)

In [12]: numbers
Out[12]: {4, 6, 8, 10, 12, 21, 23, 45, 90}
```

```python
In [2]: numbers = {1, 4, 8, 9, 3, 5, 6, 0, 12, 11, 19, 15, 13, 10}

In [3]: numbers
Out[3]: {0, 1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 19}

In [4]: for number in numbers:
   ...:     print(number)
   ...: 
0
1
3
4
5
6
8
9
10
11
12
13
15
19

In [5]: numbers.add(34)

In [6]: numbers
Out[6]: {0, 1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 19, 34}

In [7]: numbers.add(7)

In [8]: numbers
Out[8]: {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 19, 34}

In [9]: for number in numbers:
   ...:     print(number)
   ...: 
0
1
34
3
4
5
6
7
8
9
10
11
12
13
15
19

In [10]: numbers.pop()
Out[10]: 0

In [11]: numbers.pop()
Out[11]: 1

In [12]: numbers.pop()
Out[12]: 34

In [13]: numbers.pop()
Out[13]: 3

In [14]: numbers.pop()
Out[14]: 4

In [15]: numbers.pop()
Out[15]: 5

In [16]: numbers.pop()
Out[16]: 6

In [17]: numbers.pop()
Out[17]: 7

In [18]: numbers.pop()
Out[18]: 8

In [19]: numbers
Out[19]: {9, 10, 11, 12, 13, 15, 19}

In [20]: numbers.add(88)

In [21]: numbers.add(50)

In [22]: numbers.add(11)

In [23]: numbers
Out[23]: {9, 10, 11, 12, 13, 15, 19, 50, 88}

In [24]: numbers.pop()
Out[24]: 9

In [25]: numbers.pop()
Out[25]: 10

In [26]: numbers.pop()
Out[26]: 11

In [27]: numbers.pop()
Out[27]: 12

In [28]: numbers.pop()
Out[28]: 13

In [29]: numbers.pop()
Out[29]: 15

In [30]: numbers
Out[30]: {19, 50, 88}

In [31]: numbers.remove(88)

In [32]: numbers
Out[32]: {19, 50}

In [33]: type(numbers)
Out[33]: set
```

```python
In [1]: numbers = range(1, 21)

In [2]: numbers
Out[2]: range(1, 21)

In [3]: type(numbers)
Out[3]: range

In [4]: len(numbers)
Out[4]: 20

In [5]: for number in numbers:
   ...:     print(number)
   ...: 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

In [6]: even_numbers = range(0, 23, 2)

In [7]: even_numbers
Out[7]: range(0, 23, 2)

In [8]: list(even_numbers)
Out[8]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

In [9]: list(numbers)
Out[9]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

In [10]: s1 = set(even_numbers)

In [12]: s2 = set(numbers)

In [13]: s1
Out[13]: {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22}

In [14]: s2
Out[14]: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

In [15]: s1 & s2
Out[15]: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

In [16]: s1 - s2
Out[16]: {0, 22}

In [17]: s2 - s1
Out[17]: {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

In [18]: 
```

```python
In [19]: s1.issuperset(s2)
Out[19]: False

In [20]: s2.issuperset(s1)
Out[20]: False

In [21]: {1, 3, 5, 6, 7}.issuperset({5, 6})
Out[21]: True

In [22]: {1, 3, 5, 6, 7}.issuperset({5, 6, 7})
Out[22]: True

In [23]: {1, 3, 5, 6, 7}.issuperset({5, 6, 7, 8})
Out[23]: False

In [24]: {1, 3, 5, 6, 7}.issuperset({5, 6, 7, 1})
Out[24]: True

In [25]: {5, 6, 7, 1}.issubset({1, 3, 5, 6, 7})
Out[25]: True

In [26]: {1, 2, 3}.union({5, 6})
Out[26]: {1, 2, 3, 5, 6}

In [27]: {1, 2, 3} | {5, 6}
Out[27]: {1, 2, 3, 5, 6}

In [28]: {5, 6}.pop()
Out[28]: 5

In [29]: {5, 6}.pop()
Out[29]: 5

In [30]: {5, 6, 1, 0}.pop()
Out[30]: 0

In [31]: {5, 6, 1, 0, -2, -1}.pop()
Out[31]: 0

In [32]: {5, 6, 1, 0, -2, -1}.pop()
Out[32]: 0

In [34]: {5, 6, 1,11, -2, -1}.pop()
Out[34]: 1

In [35]: 

In [35]: {5, 6, 1,11, -2, -1}.pop()
Out[35]: 1

In [36]: {5, 6, 1, 11, -2, -1, 6}.pop()
Out[36]: 1

In [37]: {5, 6, 90, 1, 11, -2, -1, 6}.pop()
Out[37]: 1
```

```python
In [1]: odd_numbers = {11, 5, 3, 1, 9, 7}

In [2]: even_numbers = {2, 4, 8, 6, 10, 14}

In [3]: print(odd_numbers)
{1, 3, 5, 7, 9, 11}

In [4]: odd_numbers
Out[4]: {1, 3, 5, 7, 9, 11}

In [5]: print(even_numbers)
{2, 4, 6, 8, 10, 14}

In [6]: even_numbers
Out[6]: {2, 4, 6, 8, 10, 14}

In [7]: zip_obj = zip(even_numbers, odd_numbers)

In [8]: zip_obj
Out[8]: <zip at 0x1177c7d80>

In [9]: list(zip_obj)
Out[9]: [(2, 1), (4, 3), (6, 5), (8, 7), (10, 9), (14, 11)]

In [10]: for tup in zip_obj:
    ...:     print(tup)
    ...: 

In [11]: zip_obj = zip(even_numbers, odd_numbers)

In [12]: for tup in zip_obj:
    ...:     print(tup)
    ...: 
(2, 1)
(4, 3)
(6, 5)
(8, 7)
(10, 9)
(14, 11)

In [13]: for tup in zip_obj:
    ...:     print(tup)
    ...: 
```

```python
In [1]: points = set()

In [2]: points
Out[2]: set()

In [3]: points.add(9)

In [4]: points
Out[4]: {9}

In [5]: points.add(10)

In [6]: points
Out[6]: {9, 10}

In [7]: sum(points)
Out[7]: 19

In [8]: points.pop()
Out[8]: 9

In [9]: points.pop()
Out[9]: 10
```

```python
In [11]: points = {2, 0, 5, 3, -1, 6, 8, 91, 100}

In [12]: points
Out[12]: {-1, 0, 2, 3, 5, 6, 8, 91, 100}

In [13]: points.pop()
Out[13]: 0

In [14]: points.pop()
Out[14]: 2

In [15]: points.pop()
Out[15]: 3

In [16]: points.pop()
Out[16]: 100

In [17]: points.pop()
Out[17]: 5

In [18]: points.pop()
Out[18]: 6

In [19]: points.pop()
Out[19]: 8

In [20]: points.pop()
Out[20]: 91

In [21]: points.pop()
Out[21]: -1
```

```python
In [46]: for number in set([1, 5, 7, 9, 11, 45, 56, 78]):
    ...:     print(f"number -> {number}")
    ...: 
number -> 1
number -> 5
number -> 7
number -> 9
number -> 11
number -> 45
number -> 78
number -> 56

In [47]: set([1, 5, 7, 9, 11, 45, 56, 78])
Out[47]: {1, 5, 7, 9, 11, 45, 56, 78}
```

```python
In [50]: frozenset([1, 5, 7, 9, 11, 45, 56, 78])
Out[50]: frozenset({1, 5, 7, 9, 11, 45, 56, 78})

In [51]: frozenset("Apple")
Out[51]: frozenset({'A', 'e', 'l', 'p'})

In [52]: for ch in frozenset("Apple"):
    ...:     print(ch)
    ...: 
p
l
A
e
```

```python
In [53]: {"Apple", "Boy", "Python", "October", "My", "State"}.pop()
Out[53]: 'My'

In [54]: {"Apple", "Boy", "C", "Python", "October", "My", "State"}.pop()
Out[54]: 'My'

In [55]: {"Apple", "Boy", "C", "Python", "October", "My", "Pi", "State"}.pop()
Out[55]: 'Pi'

In [56]: {"Apple", "Boy", "C", "Python", "October", "My", "Pi", "D", "State"}.pop()
Out[56]: 'Pi'

In [57]: {"Apple", "Boy", "C", "Python", "October", "My", "Pi", "C", "State"}.pop()
Out[57]: 'Pi'

In [58]: {"Apple", "Boy", "C", "Python", "October", "My", "Pi", "Cc", "State"}.pop()
Out[58]: 'Cc'

In [59]: {"Apple", "Boy", "C", "Python", "October", "My", "Pi", "pc", "State"}.pop()
Out[59]: 'Pi'

In [60]: {"Apple", "Boy", "C", "Python", "October", "My", "Pi", "pc", "State"}.pop()
Out[60]: 'Pi'

In [61]: {"Apple", "Boy", "C", "Python", "October", "My", "Pi", "pc", "State"}.pop()
Out[61]: 'Pi'

In [62]: {"Apple", "Boy", "C", "Python", "October", "My", "Pi", "Pc", "State"}.pop()
Out[62]: 'Pi'

In [63]: {"Apple", "Boy", "C", "Python", "October", "My", "Pi", "Hi", "State"}.pop()
Out[63]: 'Pi'
```

```python
In [64]: {1, 5, 6}.discard(6)

In [65]: s = {1, 5, 6}

In [66]: s.discard(6)
```

```python
In [68]: s
Out[68]: {1, 5}

In [69]: s = {1, 5, 6, 10, 6, 56, 1, 6, 11}

In [70]: s
Out[70]: {1, 5, 6, 10, 11, 56}

In [71]: s.discard(1)

In [72]: s
Out[72]: {5, 6, 10, 11, 56}
```

```python

In [73]: {1, 6, 7} & {12, 5, 7}
Out[73]: {7}

In [74]: {1, 6, 7} & {12, 5}
Out[74]: set()
```