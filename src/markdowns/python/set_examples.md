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