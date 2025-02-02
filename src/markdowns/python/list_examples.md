```python
In [1]: numbers = [1, 4, 5, 6, 7, 8, 12, 34, 1, 90, 42, 64, 121, 26, 45, 9, 34]

In [2]: even_numbers = [number for number in numbers if number % 2 == 0]

In [3]: even_numbers
Out[3]: [4, 6, 8, 12, 34, 90, 42, 64, 26, 34]

In [4]: odd_numbers = [number for number in numbers if number % 2 != 0]

In [5]: odd_numbers
Out[5]: [1, 5, 7, 1, 121, 45, 9]

In [6]: even_numbers + odd_numbers
Out[6]: [4, 6, 8, 12, 34, 90, 42, 64, 26, 34, 1, 5, 7, 1, 121, 45, 9]
```

```python
In [7]: even_numbers.append(200) or 1000 + odd_numbers.append(99) or 2000
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[7], line 1
----> 1 even_numbers.append(200) or 1000 + odd_numbers.append(99) or 2000

TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

In [8]: (even_numbers.append(200) or 1000) + (odd_numbers.append(99) or 2000)
Out[8]: 3000
```

```python
In [9]: odd_numbers
Out[9]: [1, 5, 7, 1, 121, 45, 9, 99, 99]

In [10]: odd_numbers
Out[10]: [1, 5, 7, 1, 121, 45, 9, 99, 99]

In [11]: even_numbers
Out[11]: [4, 6, 8, 12, 34, 90, 42, 64, 26, 34, 200, 200]

In [12]: odd_numbers = set(odd_numbers)

In [13]: even_numbers = set(even_numbers)

In [14]: odd_numbers
Out[14]: {1, 5, 7, 9, 45, 99, 121}

In [15]: even_numbers
Out[15]: {4, 6, 8, 12, 26, 34, 42, 64, 90, 200}
```

```python
In [1]: numbers = [1, 4, 6, 8, 12, 90, 45, 23, 21, 24., 9, 10]

In [2]: numbers
Out[2]: [1, 4, 6, 8, 12, 90, 45, 23, 21, 24.0, 9, 10]

In [3]: while numbers:
   ...:     print(numbers.pop())
   ...: 
10
9
24.0
21
23
45
90
12
8
6
4
1

In [4]: numbers
Out[4]: []
```

```python
In [5]: even_numbers = list()

In [6]: even_numbers
Out[6]: []

In [7]: even_numbers.append(12)

In [8]: even_numbers.append(14)

In [9]: even_numbers.append(2)

In [10]: even_numbers.extend([6, 80, 34, 22])

In [11]: even_numbers
Out[11]: [12, 14, 2, 6, 80, 34, 22]

In [12]: even_numbers.append(88)

In [13]: even_numbers
Out[13]: [12, 14, 2, 6, 80, 34, 22, 88]

In [14]: while numbers[::-1]:
    ...:     print(numbers.pop())
    ...: 

In [15]: while even_numbers[::-1]:
    ...:     print(even_numbers.pop())
    ...: 
88
22
34
80
6
2
14
12

In [16]: even_numbers
Out[16]: []

In [17]: even_numbers = [12, 14, 2, 6, 80, 34, 22, 88]

In [18]: even_numbers[::-1].pop()
Out[18]: 12

In [19]: even_numbers[::-1].pop()
Out[19]: 12

In [20]: even_numbers
Out[20]: [12, 14, 2, 6, 80, 34, 22, 88]
```

```python
In [21]: list() == []
Out[21]: True

In [22]: list() + list() + list()
Out[22]: []

In [23]: id(list()) == id([])
Out[23]: True

In [24]: id([])
Out[24]: 140489325189000

In [25]: id(list())
Out[25]: 140489595582152

In [26]: 140489325189000 == 140489595582152
Out[26]: False

In [27]: id(list()) == id([])
Out[27]: True

In [28]: id(list()) == id([])
Out[28]: True

In [29]: print(id(list()), id([]))
140489872681992 140489872681992

In [30]: 140489872681992 == 140489872681992
Out[30]: True

In [31]: print(id(list()), id([]))
140489325215624 140489325215624

In [32]: print(id(list()), id([]))
140489872541448 140489872541448

In [33]: print(id(list()), id([]))
140489325194056 140489325194056

In [34]: print(id(list()))
140488782975816

In [35]: print(id([]))
140489457264520
```
