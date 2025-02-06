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