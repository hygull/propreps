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

```python
In [14]: def print_numbers(a, b, c, d, **kwargs): # Arbitrary keyword arguments
    ...:     print("a ->", a)
    ...:     print("b ->", b)
    ...:     print("c ->", c)
    ...:     print("d ->", d)
    ...:     print("kwargs ->", kwargs)
    ...: 
```

```python
In [15]: print_numbers(c=30, d=40, b=20, a=10)
a -> 10
b -> 20
c -> 30
d -> 40
kwargs -> {}
```

```python
In [16]: print_numbers(c=30, d=40, b=20, a=10, e=90)
a -> 10
b -> 20
c -> 30
d -> 40
kwargs -> {'e': 90}
```

```python
In [19]: print_numbers(c=30, d=40, b=20, a=10, e=90, f=101)
a -> 10
b -> 20
c -> 30
d -> 40
kwargs -> {'e': 90, 'f': 101}
```

```python
In [20]: print_numbers(c=30, d=40, b=20, a=10, e=90, f=101, num1=44)
a -> 10
b -> 20
c -> 30
d -> 40
kwargs -> {'e': 90, 'f': 101, 'num1': 44}
```

```python
In [21]: print_numbers(c=30, d=40, b=20, a=10, e=90, f=101, num1=44, even_num=2)
a -> 10
b -> 20
c -> 30
d -> 40
kwargs -> {'e': 90, 'f': 101, 'num1': 44, 'even_num': 2}
```

```python
In [22]: print_numbers(c=30, d=40, b=20, a=10, e=90, f=101, num1=44, even_num=2, odd_num=90)
a -> 10
b -> 20
c -> 30
d -> 40
kwargs -> {'e': 90, 'f': 101, 'num1': 44, 'even_num': 2, 'odd_num': 90}
```

```python
In [23]: def print_numbers(a=10, b=40, c=60, d=100): # Default parameters
    ...:     print("a ->", a)
    ...:     print("b ->", b)
    ...:     print("c ->", c)
    ...:     print("d ->", d)
    ...: 

In [24]: print_numbers()
a -> 10
b -> 40
c -> 60
d -> 100

In [25]: print_numbers(a=777)
a -> 777
b -> 40
c -> 60
d -> 100

In [26]: print_numbers(b=999)
a -> 10
b -> 999
c -> 60
d -> 100

In [27]: print_numbers(c=666)
a -> 10
b -> 40
c -> 666
d -> 100

In [28]: print_numbers(d=222)
a -> 10
b -> 40
c -> 60
d -> 222

In [29]: print_numbers(a=444, d=222)
a -> 444
b -> 40
c -> 60
d -> 222

In [30]: print_numbers(a=444, d=222, b=111)
a -> 444
b -> 111
c -> 60
d -> 222

In [31]: print_numbers(a=444, d=222, b=111, c=888)
a -> 444
b -> 111
c -> 888
d -> 222
```