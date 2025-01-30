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