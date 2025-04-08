```python
In [14]: print(numbers)
[0, 1, 3, '3', '4', 5, '5', 6, 7, 8, 9, '11', 12, '13', '14', '100', 12, 5, 8, 90]

In [15]: help(print)


In [16]: print(numbers, "is a list", "Just see it")
[0, 1, 3, '3', '4', 5, '5', 6, 7, 8, 9, '11', 12, '13', '14', '100', 12, 5, 8, 90] is a list Just see it

In [17]: print(numbers, "is a list", "Just see it", sep="<->")
[0, 1, 3, '3', '4', 5, '5', 6, 7, 8, 9, '11', 12, '13', '14', '100', 12, 5, 8, 90]<->is a list<->Just see it

In [18]: print(numbers, "is a list", "Just see it", sep="<->", end="***---***")
[0, 1, 3, '3', '4', 5, '5', 6, 7, 8, 9, '11', 12, '13', '14', '100', 12, 5, 8, 90]<->is a list<->Just see it***---***
In [19]: print(numbers, "is a list", "Just see it", sep="<->", end=" (DONE)")
[0, 1, 3, '3', '4', 5, '5', 6, 7, 8, 9, '11', 12, '13', '14', '100', 12, 5, 8, 90]<->is a list<->Just see it (DONE)
In [20]: print(numbers, "is a list", "Just see it", sep=" <-> ", end=" (DONE)")
[0, 1, 3, '3', '4', 5, '5', 6, 7, 8, 9, '11', 12, '13', '14', '100', 12, 5, 8, 90] <-> is a list <-> Just see it (DONE)
In [21]: 
```

```python
In [4]: full_name="Rishikesh Agrawani"; first_name='Rishikesh'; last_name='Agrawani'

In [5]: "{full_name} is the combination of {first_name} and {last_name}"
Out[5]: '{full_name} is the combination of {first_name} and {last_name}'

In [6]: "{full_name} is the combination of {first_name} and {last_name}".format(full_name="Rishikesh Agrawani", first_name='Rishikesh', last_name='Agrawani')
Out[6]: 'Rishikesh Agrawani is the combination of Rishikesh and Agrawani'

In [7]: full_name="Rishikesh Agrawani"; first_name='Rishikesh'; last_name='Agrawani'

In [8]: full_name
Out[8]: 'Rishikesh Agrawani'

In [9]: first_name
Out[9]: 'Rishikesh'

In [10]: last_name
Out[10]: 'Agrawani'

In [11]: "{full_name} is the combination of {first_name} and {last_name}".format(full_name = f"{first_name} {last_name}", first_name=first_name, last_name=last_name)
Out[11]: 'Rishikesh Agrawani is the combination of Rishikesh and Agrawani'

In [12]: kwargs = {"full_name":  f"{first_name} {last_name}", "first_name": first_name, "last_name": last_name}

In [13]: kwargs
Out[13]: 
{'full_name': 'Rishikesh Agrawani',
 'first_name': 'Rishikesh',
 'last_name': 'Agrawani'}

In [14]: "{full_name} is the combination of {first_name} and {last_name}".format(**kwargs)
Out[14]: 'Rishikesh Agrawani is the combination of Rishikesh and Agrawani'
```