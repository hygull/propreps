```python
In [1]: def print_numbers(a, b, c, d):
   ...:     # All positional arguments
   ...:     print("a ->", a)
   ...:     print("b ->", b)
   ...:     print("c ->", c)
   ...:     print("d ->", d)
   ...: 

In [2]: print_numbers(45, 100, 30, 15)
a -> 45
b -> 100
c -> 30
d -> 15
```

```python
In [3]: print_numbers(d=45, c=100, b=30, a=15)
a -> 15
b -> 30
c -> 100
d -> 45
```

