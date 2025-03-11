```python
In [1]: def print_numbers(a, b, c, d):
   ...:     print("a ->", a)
   ...:     print("b ->", b)
   ...:     print("c ->", c)
   ...:     print("d ->", d)
   ...: 

In [2]: print_numbers(45, 100, 30, 15) # All positional arguments, order matters
a -> 45
b -> 100
c -> 30
d -> 15
```

```python
In [3]: print_numbers(d=45, c=100, b=30, a=15) # All keyword arguments -> order doesn't matter
a -> 15
b -> 30
c -> 100
d -> 45

In [4]: print_numbers(c=30, d=40, b=20, a=10) # All keyword arguments -> order doesn't matter
a -> 10
b -> 20
c -> 30
d -> 40
```

```python
In [5]: def print_numbers(a, b, c, d, *args): # Arbitrary arguments
   ...:     print("a ->", a)
   ...:     print("b ->", b)
   ...:     print("c ->", c)
   ...:     print("d ->", d)
   ...:     print("args ->", args)
   ...: 

In [6]: print_numbers(45, 100, 30, 15)
a -> 45
b -> 100
c -> 30
d -> 15
args -> ()

In [7]: print_numbers(c=30, d=40, b=20, a=10)
a -> 10
b -> 20
c -> 30
d -> 40
args -> ()

In [8]: print_numbers(c=30, d=40, b=20, a=10)
a -> 10
b -> 20
c -> 30
d -> 40
args -> ()

In [9]: print_numbers(45, 100, 30, 15, 80)
a -> 45
b -> 100
c -> 30
d -> 15
args -> (80,)

In [10]: print_numbers(45, 100, 30, 15, 80, 90)
a -> 45
b -> 100
c -> 30
d -> 15
args -> (80, 90)

In [11]: print_numbers(45, 100, 30, 15, 80, 90, 23)
a -> 45
b -> 100
c -> 30
d -> 15
args -> (80, 90, 23)
```