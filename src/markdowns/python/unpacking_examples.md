```python
In [1]: numbers = [1, 4, 6, 8, 12, 90, 45, 23, 21, 24., 9, 10]

In [2]: one, *random_numbers, ten = numbers

In [3]: one
Out[3]: 1

In [4]: random_numbers
Out[4]: [4, 6, 8, 12, 90, 45, 23, 21, 24.0, 9]

In [5]: ten
Out[5]: 10

In [6]: 

In [6]: even_numbers = (2, 4, 10)

In [7]: two, four, ten = even_numbers

In [8]: four, ten, two
Out[8]: (4, 10, 2)
```

```python
In [9]: details = ("Rishikesh", ("Agrawani", 32))

In [10]: first_name, (last_name, age) = details # Nested unpacking tuple

In [11]: first_name
Out[11]: 'Rishikesh'

In [12]: last_name
Out[12]: 'Agrawani'

In [13]: age
Out[13]: 32

In [14]: details2 = ["Rishikesh", ("Agrawani", 32)]

In [15]: first_name, (last_name, age) = details # Nested unpacking list with tuple

In [16]: age
Out[16]: 32

In [17]: details2 = ["Rishikesh", ["Agrawani", 32]]

In [18]: first_name, (last_name, age) = details # Nested unpacking list with list

In [19]: last_name
Out[19]: 'Agrawani'

In [20]: first_name, [last_name, age] = details # Nested unpacking list with list

In [21]: last_name
Out[21]: 'Agrawani'
```

```python
In [3]: (a, b) = 67, 89

In [4]: a
Out[4]: 67

In [5]: b
Out[5]: 89

In [6]: ((a, b), c) = (12, 56), 9

In [7]: ((a2, b2), c2) = (11, 55), 8,

In [8]: a
Out[8]: 12

In [9]: b
Out[9]: 56

In [10]: c
Out[10]: 9

In [11]: a2
Out[11]: 11

In [12]: b2
Out[12]: 55

In [13]: c2
Out[13]: 8

In [14]: ((a3, b3), c3) = ((11, 55), 8)

In [15]: a3
Out[15]: 11

In [16]: b3, c3
Out[16]: (55, 8)

In [17]: b3, c3,
Out[17]: (55, 8)

In [18]: x, y = [23, 67]

In [19]: x
Out[19]: 23

In [20]: y
Out[20]: 67
```