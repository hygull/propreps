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

### Positional-Only arguments

```python
In [34]: def print_numbers(a, b):
    ...:     print("a ->", a)
    ...:     print("b ->", b)
    ...: 

In [35]: print_numbers(a=444, b=222)
a -> 444
b -> 222
```

```python
In [36]: # Positional-Only arguments

In [37]: def print_numbers(a, b, /):
    ...:     print("a ->", a)
    ...:     print("b ->", b)
    ...: 
```

```python
In [38]: print_numbers(a=444, b=222)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[38], line 1
----> 1 print_numbers(a=444, b=222)

TypeError: print_numbers() got some positional-Only arguments passed as keyword arguments: 'a, b'
```

```python
In [39]: print_numbers(444, 222)
a -> 444
b -> 222
```

```python
In [40]: print_numbers(444, b=222)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[40], line 1
----> 1 print_numbers(444, b=222)

TypeError: print_numbers() got some positional-Only arguments passed as keyword arguments: 'b'
```

### Keyword-Only arguments

```python
In [41]: # Keyword-Only arguments

In [42]: def print_numbers(*, a, b):
    ...:     print("a ->", a)
    ...:     print("b ->", b)
    ...: 

In [43]: print_numbers(444, b=222)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[43], line 1
----> 1 print_numbers(444, b=222)

TypeError: print_numbers() takes 0 positional arguments but 1 positional argument (and 1 keyword-Only argument) were given
```

```python
In [44]: print_numbers(a=444, b=222)
a -> 444
b -> 222
```

```python
In [45]: print_numbers(b=333, a=888)
a -> 888
b -> 333
```

```python
In [46]: print_numbers(1, 5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[46], line 1
----> 1 print_numbers(1, 5)

TypeError: print_numbers() takes 0 positional arguments but 2 were given
```

### To know more about the different use cases of calling the function

```python
In [47]: def print_numbers(a, b, c, d):
    ...:     print("a ->", a)
    ...:     print("b ->", b)
    ...:     print("c ->", c)
    ...:     print("d ->", d)
    ...: 

In [48]: print_numbers(a=10, b=20, c=30, d=40)
a -> 10
b -> 20
c -> 30
d -> 40
```

```python
In [49]: print_numbers(100, 200, c=30, d=40)
a -> 100
b -> 200
c -> 30
d -> 40
```

```python
In [50]: print_numbers(100, 200, 300, d=40)
a -> 100
b -> 200
c -> 300
d -> 40
```

```python
In [51]: print_numbers(100, 200, 300, 400)
a -> 100
b -> 200
c -> 300
d -> 400
```

```python
In [52]: print_numbers(a=100, 200, 300, 400)
  Cell In[52], line 1
    print_numbers(a=100, 200, 300, 400)
                                      ^
SyntaxError: positional argument follows keyword argument
```

```python
In [53]: print_numbers(d=111, b=222, a=444, c=555)
a -> 444
b -> 222
c -> 555
d -> 111
```

```python
In [54]: print_numbers(d=111, b=222, a=444, c=555, d=90)
  Cell In[54], line 1
    print_numbers(d=111, b=222, a=444, c=555, d=90)
                                              ^
SyntaxError: keyword argument repeated: d
```

```python
In [55]: print_numbers(111, b=222, a=444, c=555, a=90)
  Cell In[55], line 1
    print_numbers(111, b=222, a=444, c=555, a=90)
                                            ^
SyntaxError: keyword argument repeated: a
```

### Combine Positional-Only and Keyword-Only

```python
In [58]: def print_numbers(a, b, /, *, c, d):
    ...:     print("a ->", a)
    ...:     print("b ->", b)
    ...:     print("c ->", c)
    ...:     print("d ->", d)
    ...: 

In [59]: print_numbers(a=111, b=222, d=444, c=555)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[59], line 1
----> 1 print_numbers(a=111, b=222, d=444, c=555)
```

```python
TypeError: print_numbers() got some positional-only arguments passed as keyword arguments: 'a, b'

In [60]: print_numbers(111, 222, d=444, c=555)
a -> 111
b -> 222
c -> 555
d -> 444
```

```python
In [61]: print_numbers(111, 222, c=444, d=555)
a -> 111
b -> 222
c -> 444
d -> 555
```

```python
In [62]: print_numbers(111, 222, 444, d=555)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[62], line 1
----> 1 print_numbers(111, 222, 444, d=555)

TypeError: print_numbers() takes 2 positional arguments but 3 positional arguments (and 1 keyword-only argument) were given
```