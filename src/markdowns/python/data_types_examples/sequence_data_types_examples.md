```python
In [1]: # list

In [2]: l = [1, 4, 6, 8, 9, 34, 5, -1 , "Apple", 67.01, 5+9J]

In [3]: l
Out[3]: [1, 4, 6, 8, 9, 34, 5, -1, 'Apple', 67.01, (5+9j)]

In [4]: l[0]
Out[4]: 1

In [5]: l[-1]
Out[5]: (5+9j)

In [6]: l[5]
Out[6]: 34

In [7]: l.append(78)

In [8]: l
Out[8]: [1, 4, 6, 8, 9, 34, 5, -1, 'Apple', 67.01, (5+9j), 78]

In [9]: # tuple

In [10]: t = (12, 6, 89.0, 89.44, 4+4j, "Banana")

In [11]: t
Out[11]: (12, 6, 89.0, 89.44, (4+4j), 'Banana')
```


```python
In [12]: # bytearray

In [13]: b_arr = bytearray("Apple")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[13], line 1
----> 1 b_arr = bytearray("Apple")

TypeError: string argument without an encoding
```

```python
In [14]: b_arr = bytearray(b"Apple")

In [15]: b_arr
Out[15]: bytearray(b'Apple')

In [16]: b_arr[0]
Out[16]: 65

In [17]: b_arr[1]
Out[17]: 112

In [18]: for ch in b_arr:
    ...:     print(ch)
    ...: 
65
112
112
108
101

In [19]: for ch in b_arr:
    ...:     print(ch, '->', chr(ch))
    ...: 
65 -> A
112 -> p
112 -> p
108 -> l
101 -> e

In [20]: for ch in "Apple":
    ...:     print(ch, '->', ord(ch))
    ...: 
A -> 65
p -> 112
p -> 112
l -> 108
e -> 101

In [21]: for index, ch in enumerate(b_arr):
    ...:     print(index, ch, '->', chr(ch))
    ...: 
0 65 -> A
1 112 -> p
2 112 -> p
3 108 -> l
4 101 -> e
```

```python
In [22]: b_arr[5] = 66
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[22], line 1
----> 1 b_arr[5] = 66

IndexError: bytearray index out of range
```

```python
In [23]: b_arr.append(66)

In [24]: b_arr.append(97)

In [25]: b_arr
Out[25]: bytearray(b'AppleBa')
```