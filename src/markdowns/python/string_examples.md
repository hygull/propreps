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
