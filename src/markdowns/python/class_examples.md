```python
In [52]: class A:
    ...:     p = 11
    ...:     q = 22
    ...:     r = 33
    ...: 

In [53]: a = A()

In [54]: getattr(a, 'p')
Out[54]: 11

In [55]: getattr(a, 'q')
Out[55]: 22

In [56]: getattr(a, 'r')
Out[56]: 33

In [57]: setattr(a, 'r', 44)

In [58]: a.r
Out[58]: 44

In [59]: a
Out[59]: <__main__.A at 0x10f4e4500>

In [60]: a.__dict__
Out[60]: {'r': 44}

In [61]: a.p
Out[61]: 11

In [62]: a.q
Out[62]: 22
```

```python
In [63]: getattr(a, 'r2')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[63], line 1
----> 1 getattr(a, 'r2')

AttributeError: 'A' object has no attribute 'r2'

In [64]: getattr(a, 'r2', 'Nothing')
Out[64]: 'Nothing'
```