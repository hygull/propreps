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