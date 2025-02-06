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