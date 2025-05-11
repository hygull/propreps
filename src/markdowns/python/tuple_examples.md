```python
In [1]: ()
Out[1]: ()

In [2]: type(())
Out[2]: tuple

In [3]: (1)
Out[3]: 1

In [4]: (1,)
Out[4]: (1,)

In [5]: type((1))
Out[5]: int

In [6]: type((1,))
Out[6]: tuple

In [7]: (1,) + (2, ) + (3, 4)
Out[7]: (1, 2, 3, 4)

In [8]: (1,) + (2, ) + (3, 4) + (5, 6, 7, )
Out[8]: (1, 2, 3, 4, 5, 6, 7)
```

```python
In [11]: (1, 5, 7, 8, 9, 10, 3, 4, 9, 1, 7, 10, 9).count(9)
Out[11]: 3

In [12]: (1, 5, 7, 8, 9, 10, 3, 4, 9, 1, 7, 10, 9).count(10)
Out[12]: 2

In [13]: (1, 5, 7, 8, 9, 10, 3, 4, 9, 1, 7, 10, 9).count(3)
Out[13]: 1

In [14]: (1, 5, 7, 8, 9, 10, 3, 4, 9, 1, 7, 10, 9).index(3)
Out[14]: 6

In [15]: (1, 5, 7, 8, 9, 10, 3, 4, 9, 1, 7, 10, 9).index(10)
Out[15]: 5

In [16]: (1, 5, 7, 8, 9, 10, 3, 4, 9, 1, 7, 10, 9).index(9)
Out[16]: 4
```

```python
In [1]: (1, 4) + tuple()
Out[1]: (1, 4)

In [2]: (1, 4) + tuple() + tuple("ABC")
Out[2]: (1, 4, 'A', 'B', 'C')

In [3]: (1, 4) + tuple() + tuple(["ABC"])
Out[3]: (1, 4, 'ABC')

In [4]: (1, 4) + tuple() + tuple([11, 67, 89, 0])
Out[4]: (1, 4, 11, 67, 89, 0)
```


```python
In [5]: 1 in (1,)
Out[5]: True

In [6]: 1 in (1, 3)
Out[6]: True

In [7]: 1 in (1, 3, 89)
Out[7]: True

In [8]: 89 not in (1, 3, 89)
Out[8]: False

In [9]: not 89 in (1, 3, 89)
Out[9]: False

In [10]: 1 in tuple(range(1, 10))
Out[10]: True

In [11]: "i" in tuple("Rishikesh")
Out[11]: True

In [12]: "I" in tuple("Rishikesh")
Out[12]: False

In [13]: "R" in tuple("Rishikesh")
Out[13]: True

In [14]: "R" in "Rishikesh"
Out[14]: True
```

```python
In [1]: words = ("This", "Friday", "Was Finalised", "For Release!")

In [2]: words2 = ("But", "That shpuld not be done!")

In [3]: words
Out[3]: ('This', 'Friday', 'Was Finalised', 'For Release!')

In [4]: words2
Out[4]: ('But', 'That shpuld not be done!')

In [5]: words + words2
Out[5]: 
('This',
 'Friday',
 'Was Finalised',
 'For Release!',
 'But',
 'That shpuld not be done!')

In [6]: " ".join(words + words2)
Out[6]: 'This Friday Was Finalised For Release! But That shpuld not be done!'
```

```python
In [1]: (True, 56.99, "Wow, Python!", 14+1992J, 5, set([1, 5, 7]))
Out[1]: (True, 56.99, 'Wow, Python!', (14+1992j), 5, {1, 5, 7})

In [2]: tup = (True, 56.99, "Wow, Python!", 14+1992J, 5, set([1, 5, 7]))

In [4]: for item in tup:
   ...:     print(tup, "->", type(item))
   ...: 
(True, 56.99, 'Wow, Python!', (14+1992j), 5, {1, 5, 7}) -> <class 'bool'>
(True, 56.99, 'Wow, Python!', (14+1992j), 5, {1, 5, 7}) -> <class 'float'>
(True, 56.99, 'Wow, Python!', (14+1992j), 5, {1, 5, 7}) -> <class 'str'>
(True, 56.99, 'Wow, Python!', (14+1992j), 5, {1, 5, 7}) -> <class 'complex'>
(True, 56.99, 'Wow, Python!', (14+1992j), 5, {1, 5, 7}) -> <class 'int'>
(True, 56.99, 'Wow, Python!', (14+1992j), 5, {1, 5, 7}) -> <class 'set'>
```