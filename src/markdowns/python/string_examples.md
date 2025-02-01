```python
In [1]: first_name = "Rishikesh"

In [2]: for ch in first_name:
   ...:     print(ch)
   ...: 
R
i
s
h
i
k
e
s
h

In [3]: for ch in first_name[::-1]:
   ...:     print(ch)
   ...: 
h
s
e
k
i
h
s
i
R

In [4]: first_name
Out[4]: 'Rishikesh'

In [5]: first_name[:]
Out[5]: 'Rishikesh'

In [6]: first_name[::-1]
Out[6]: 'hsekihsiR'
```

```python
In [7]: i = 0

In [8]: while i < len(first_name):
   ...:     print(first_name[i])
   ...:     i += 1
   ...: 
R
i
s
h
i
k
e
s
h

In [9]: i = len(first_name) - 1

In [10]: while i > -1:
    ...:     print(first_name[i])
    ...:     i -= 1
    ...: 
h
s
e
k
i
h
s
i
R

In [11]: 
```

```python
In [11]: "Rishikesh"[:1]
Out[11]: 'R'

In [12]: "Rishikesh"[::-1]
Out[12]: 'hsekihsiR'

In [13]: "Rishikesh"[::-1] "Hemkesh"[::-1]
  File "<ipython-input-13-a4fadb83eb6b>", line 1
    "Rishikesh"[::-1] "Hemkesh"[::-1]
                              ^
SyntaxError: invalid syntax


In [14]: "Rishikesh"[::-1] + "Hemkesh"[::-1]
Out[14]: 'hsekihsiRhsekmeH'

In [15]: "Rishikesh" "Hemkesh"
Out[15]: 'RishikeshHemkesh'
```

```python
In [16]: "Rishikesh" "Hemkesh" * 5
Out[16]: 'RishikeshHemkeshRishikeshHemkeshRishikeshHemkeshRishikeshHemkeshRishikeshHemkesh'

In [18]: "Rishikesh" * len("Hemkesh")
Out[18]: 'RishikeshRishikeshRishikeshRishikeshRishikeshRishikeshRishikesh'
```
