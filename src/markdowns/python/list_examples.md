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

```python
In [1]: numbers = [1, 5, 8, 9, 12, 3, 6, 7, 0]

In [2]: numbers.sort(key=lambda number: number % 2)

In [3]: numbers
Out[3]: [8, 12, 6, 0, 1, 5, 9, 3, 7]

In [4]: numbers = [1, 5, 8, 9, 12, 3, 6, 7, 0, "13", "100", "14", "3", "5", "11", "4"]

In [5]: numbers
Out[5]: [1, 5, 8, 9, 12, 3, 6, 7, 0, '13', '100', '14', '3', '5', '11', '4']
```

```python
In [6]: numbers.sort()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-52f87dfc1b99> in <module>
----> 1 numbers.sort()

TypeError: '<' not supported between instances of 'str' and 'int'
```

```python
In [7]: numbers.sort(key=lambda number: int(number))

In [8]: numbers
Out[8]: [0, 1, 3, '3', '4', 5, '5', 6, 7, 8, 9, '11', 12, '13', '14', '100']
```

```python
In [9]: numbers
Out[9]: [0, 1, 3, '3', '4', 5, '5', 6, 7, 8, 9, '11', 12, '13', '14', '100']

In [10]: ret = numbers.extend([12, 5, 8, 90])

In [11]: ret

In [12]: print(ret)
None

In [13]: numbers
Out[13]: 
[0,
 1,
 3,
 '3',
 '4',
 5,
 '5',
 6,
 7,
 8,
 9,
 '11',
 12,
 '13',
 '14',
 '100',
 12,
 5,
 8,
 90]
```


```python
In [3]: l = [12, 56, 78, 90, 34, 21, 34, 56, 32, 13]

In [4]: l
Out[4]: [12, 56, 78, 90, 34, 21, 34, 56, 32, 13]

In [5]: l[::-1]
Out[5]: [13, 32, 56, 34, 21, 34, 90, 78, 56, 12]

In [6]: reversed(l)
Out[6]: <list_reverseiterator at 0x1054721a0>

In [7]: list(reversed(l))
Out[7]: [13, 32, 56, 34, 21, 34, 90, 78, 56, 12]

In [8]: l
Out[8]: [12, 56, 78, 90, 34, 21, 34, 56, 32, 13]

In [9]: l.reverse()

In [10]: l
Out[10]: [13, 32, 56, 34, 21, 34, 90, 78, 56, 12]
```

```python
In [2]: l = [12, 56, 78, 90, 34, 21, 34, 56, 32, 13]

In [3]: l
Out[3]: [12, 56, 78, 90, 34, 21, 34, 56, 32, 13]

In [4]: l.insert(5, 100)

In [5]: l
Out[5]: [12, 56, 78, 90, 34, 100, 21, 34, 56, 32, 13]

In [6]: l.sort()

In [7]: l
Out[7]: [12, 13, 21, 32, 34, 34, 56, 56, 78, 90, 100]

In [8]: l[::-1]
Out[8]: [100, 90, 78, 56, 56, 34, 34, 32, 21, 13, 12]

In [9]: l.append(45)

In [10]: l
Out[10]: [12, 13, 21, 32, 34, 34, 56, 56, 78, 90, 100, 45]

In [11]: l.append(46)

In [12]: l.extend([90, 4, 7, 9])

In [13]: l
Out[13]: [12, 13, 21, 32, 34, 34, 56, 56, 78, 90, 100, 45, 46, 90, 4, 7, 9]

In [14]: l.pop()
Out[14]: 9

In [15]: l.pop()
Out[15]: 7

In [16]: l
Out[16]: [12, 13, 21, 32, 34, 34, 56, 56, 78, 90, 100, 45, 46, 90, 4]

In [17]: l.index(56)
Out[17]: 6

In [18]: l[6]
Out[18]: 56

In [19]: l[7]
Out[19]: 56

In [20]: l[8]
Out[20]: 78

In [21]: l.count(56)
Out[21]: 2

In [22]: l.insert(7, 67)

In [23]: l
Out[23]: [12, 13, 21, 32, 34, 34, 56, 67, 56, 78, 90, 100, 45, 46, 90, 4]

In [24]: l.remove(56)

In [25]: l
Out[25]: [12, 13, 21, 32, 34, 34, 67, 56, 78, 90, 100, 45, 46, 90, 4]

In [26]: l2 = l.copy()

In [27]: l2
Out[27]: [12, 13, 21, 32, 34, 34, 67, 56, 78, 90, 100, 45, 46, 90, 4]

In [28]: l2[0] = 77

In [29]: l2
Out[29]: [77, 13, 21, 32, 34, 34, 67, 56, 78, 90, 100, 45, 46, 90, 4]

In [30]: l
Out[30]: [12, 13, 21, 32, 34, 34, 67, 56, 78, 90, 100, 45, 46, 90, 4]
``` 

```python
In [1]: l = [1, 4, 5, 78, 90, 93, 21, 13, 25, 22, 20, 2, 91]

In [2]: l
Out[2]: [1, 4, 5, 78, 90, 93, 21, 13, 25, 22, 20, 2, 91]

In [3]: l[::-1]
Out[3]: [91, 2, 20, 22, 25, 13, 21, 93, 90, 78, 5, 4, 1]

In [4]: l[1:]
Out[4]: [4, 5, 78, 90, 93, 21, 13, 25, 22, 20, 2, 91]

In [5]: l[1:10000]
Out[5]: [4, 5, 78, 90, 93, 21, 13, 25, 22, 20, 2, 91]

In [6]: l[1:2]
Out[6]: [4]

In [7]: l[:2]
Out[7]: [1, 4]

In [8]: l.pop()
Out[8]: 91

In [9]: l
Out[9]: [1, 4, 5, 78, 90, 93, 21, 13, 25, 22, 20, 2]

In [10]: len(l)
Out[10]: 12

In [11]: l.count(13)
Out[11]: 1

In [12]: l.append(4)

In [13]: l
Out[13]: [1, 4, 5, 78, 90, 93, 21, 13, 25, 22, 20, 2, 4]

In [14]: l.count(4)
Out[14]: 2

In [15]: l.append(4)

In [16]: l
Out[16]: [1, 4, 5, 78, 90, 93, 21, 13, 25, 22, 20, 2, 4, 4]

In [17]: l.count(4)
Out[17]: 3

In [18]: l.index(4)
Out[18]: 1

In [19]: l.remove(l.index(4))

In [20]: l
Out[20]: [4, 5, 78, 90, 93, 21, 13, 25, 22, 20, 2, 4, 4]

In [21]: l.remove(l.index(4))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-21-76941ed5e336> in <module>
----> 1 l.remove(l.index(4))

ValueError: list.remove(x): x not in list

In [22]: l
Out[22]: [4, 5, 78, 90, 93, 21, 13, 25, 22, 20, 2, 4, 4]

In [23]: l.pop(1)
Out[23]: 5

In [24]: l.pop(10)
Out[24]: 4

In [25]: l.pop(10)
Out[25]: 4

In [26]: l.pop(10)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-26-906f487d7cdc> in <module>
----> 1 l.pop(10)

IndexError: pop index out of range

In [27]: l.pop(9)
Out[27]: 2

In [28]: 
```

```python
In [28]: l
Out[28]: [4, 78, 90, 93, 21, 13, 25, 22, 20]

In [29]: len(l)
Out[29]: 9

In [30]: l[0]
Out[30]: 4

In [31]: l[-1]
Out[31]: 20

In [32]: l[-12]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-32-8d08c506af38> in <module>
----> 1 l[-12]

IndexError: list index out of range

In [33]: l[-2]
Out[33]: 22

In [34]: l[-3]
Out[34]: 25

In [35]: l[-4]
Out[35]: 13

In [36]: l[-4: -1]
Out[36]: [13, 25, 22]

In [37]: l[-4: 0]
Out[37]: []

In [38]: l[-4: ]
Out[38]: [13, 25, 22, 20]

In [39]: l[-4: -5]
Out[39]: []
```

```python
In [2]: chars = ["R"] + list("ishikesh")

In [3]: chars
Out[3]: ['R', 'i', 's', 'h', 'i', 'k', 'e', 's', 'h']

In [4]: print(chars)
['R', 'i', 's', 'h', 'i', 'k', 'e', 's', 'h']

In [5]: print("-".join(chars))
R-i-s-h-i-k-e-s-h

In [6]: print("<->>".join(chars))
R<->>i<->>s<->>h<->>i<->>k<->>e<->>s<->>h

In [7]: print("<->".join(chars))
R<->i<->s<->h<->i<->k<->e<->s<->h

In [8]: s = "<->".join(chars)

In [9]: print(s)
R<->i<->s<->h<->i<->k<->e<->s<->h

In [10]: len(s)
Out[10]: 33

In [11]: s.replace("<->", "")
Out[11]: 'Rishikesh'

In [12]: s
Out[12]: 'R<->i<->s<->h<->i<->k<->e<->s<->h'

In [13]: list(s)
Out[13]: 
['R',
 '<',
 '-',
 '>',
 'i',
 '<',
 '-',
 '>',
 's',
 '<',
 '-',
 '>',
 'h',
 '<',
 '-',
 '>',
 'i',
 '<',
 '-',
 '>',
 'k',
 '<',
 '-',
 '>',
 'e',
 '<',
 '-',
 '>',
 's',
 '<',
 '-',
 '>',
 'h']

In [14]: print(list(s))
['R', '<', '-', '>', 'i', '<', '-', '>', 's', '<', '-', '>', 'h', '<', '-', '>', 'i', '<', '-', '>', 'k', '<', '-', '>', 'e', '<', '-', '>', 's', '<', '-', '>', 'h']

In [15]: 
```


```python
In [14]: first, *rest, last = [1, 56, 34, 21, 89, 10, 100]

In [15]: rest
Out[15]: [56, 34, 21, 89, 10]

In [16]: first
Out[16]: 1

In [17]: last
Out[17]: 100

In [18]: len(rest)
Out[18]: 5

In [19]: rest.append(101)

In [21]: rest.insert(len(rest) - 1, 102)

In [22]: rest
Out[22]: [56, 34, 21, 89, 10, 102, 101]

In [23]: rest.insert(len(rest) - 1, 103)

In [24]: rest
Out[24]: [56, 34, 21, 89, 10, 102, 103, 101]

In [25]: rest.insert(len(rest), 103)

In [26]: rest
Out[26]: [56, 34, 21, 89, 10, 102, 103, 101, 103]

In [27]: rest.insert(len(rest), 104)

In [28]: rest
Out[28]: [56, 34, 21, 89, 10, 102, 103, 101, 103, 104]

In [29]: rest.extend({12, 67, 89, 1, 3,})

In [30]: rest
Out[30]: [56, 34, 21, 89, 10, 102, 103, 101, 103, 104, 1, 67, 3, 89, 12]

In [31]: rest.extend({1: "one", 2: "two", 201: "two_zero_one"})

In [32]: rest
Out[32]: [56, 34, 21, 89, 10, 102, 103, 101, 103, 104, 1, 67, 3, 89, 12, 1, 2, 201]
```

```python
In [1]: numbers = []

In [2]: numbers.append(90)

In [3]: numbers
Out[3]: [90]

In [4]: numbers.extend([11, 45, 67])

In [5]: numbers
Out[5]: [90, 11, 45, 67]

In [6]: numbers.extend([10, 9, 8])

In [7]: numbers
Out[7]: [90, 11, 45, 67, 10, 9, 8]

In [8]: numbers[:-1]
Out[8]: [90, 11, 45, 67, 10, 9]

In [9]: numbers[:]
Out[9]: [90, 11, 45, 67, 10, 9, 8]

In [10]: numbers[0:]
Out[10]: [90, 11, 45, 67, 10, 9, 8]

In [11]: numbers[::-1]
Out[11]: [8, 9, 10, 67, 45, 11, 90]
```

```python
In [12]: numbers.pop()
Out[12]: 8

In [13]: numbers.pop()
Out[13]: 9

In [14]: numbers.pop()
Out[14]: 10

In [15]: numbers.pop()
Out[15]: 67

In [16]: numbers.insert(-1, 77)

In [17]: numbers
Out[17]: [90, 11, 77, 45]

In [18]: numbers.insert(-1, 88)

In [19]: numbers
Out[19]: [90, 11, 77, 88, 45]

In [20]: numbers.insert(len(numbers), 987)

In [21]: numbers
Out[21]: [90, 11, 77, 88, 45, 987]
```

```python
In [30]: l = [5] * 5

In [31]: l
Out[31]: [5, 5, 5, 5, 5]

In [32]: l[0] = 10

In [33]: l
Out[33]: [10, 5, 5, 5, 5]

In [34]: l2 = [[5]] * 5

In [35]: l2
Out[35]: [[5], [5], [5], [5], [5]]

In [36]: l2[0][0] = 11

In [37]: l2
Out[37]: [[11], [11], [11], [11], [11]]
```

```python
In [9]: [0, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]
Out[9]: [0, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]

In [10]: l = [0, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]

In [11]: l
Out[11]: [0, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]

In [12]: l[-1]
Out[12]: [12, 5, 6, 7, 8]

In [13]: l[0]
Out[13]: 0

In [14]: l2 = l

In [15]: l2[0] = 90

In [16]: l
Out[16]: [90, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]

In [17]: l2
Out[17]: [90, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]

In [18]: 

In [18]: l3 = l[::-1]

In [19]: l3
Out[19]: [[12, 5, 6, 7, 8], 0, 9, 8, 7, 6, 5, 90]

In [20]: l3[0] = 99

In [21]: l3
Out[21]: [99, 0, 9, 8, 7, 6, 5, 90]

In [22]: l
Out[22]: [90, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]

In [23]: l4 = l[:]

In [24]: l4
Out[24]: [90, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]

In [25]: l4[0] = 88

In [26]: l4
Out[26]: [88, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]

In [27]: l
Out[27]: [90, 5, 6, 7, 8, 9, 0, [12, 5, 6, 7, 8]]

In [28]: l[-1]
Out[28]: [12, 5, 6, 7, 8]

In [29]: l[-1][0] = 777

In [30]: l
Out[30]: [90, 5, 6, 7, 8, 9, 0, [777, 5, 6, 7, 8]]

In [31]: l4
Out[31]: [88, 5, 6, 7, 8, 9, 0, [777, 5, 6, 7, 8]]
```

```python
In [44]: numbers = [1, 4, 6, 8, 2, 3, 4, 5, 10, 34, 100, 45, 1, 67, 89, 101]

In [45]: len(numbers)
Out[45]: 16

In [46]: numbers.pop()
Out[46]: 101

In [47]: print(numbers)
[1, 4, 6, 8, 2, 3, 4, 5, 10, 34, 100, 45, 1, 67, 89]

In [48]: len(numbers)
Out[48]: 15

In [49]: numbers.pop(1)
Out[49]: 4

In [50]: numbers
Out[50]: [1, 6, 8, 2, 3, 4, 5, 10, 34, 100, 45, 1, 67, 89]

In [51]: len(numbers)
Out[51]: 14

In [52]: numbers.append(numbers.pop(0))

In [53]: print(numbers)
[6, 8, 2, 3, 4, 5, 10, 34, 100, 45, 1, 67, 89, 1]

In [54]: len(numbers)
Out[54]: 14
```

```python
In [1]: l = [1, 4, 6, 7, 9]

In [2]: len(l)
Out[2]: 5

In [3]: l.pop(0)
Out[3]: 1

In [4]: l.append(11)

In [5]: l
Out[5]: [4, 6, 7, 9, 11]

In [6]: ret = l.append(12)

In [7]: print(ret)
None

In [8]: ret
```

```python
In [12]: l = [[1]] * 5

In [13]: l
Out[13]: [[1], [1], [1], [1], [1]]

In [14]: l[1][0] = 99

In [15]: l
Out[15]: [[99], [99], [99], [99], [99]]
```