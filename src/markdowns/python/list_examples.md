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