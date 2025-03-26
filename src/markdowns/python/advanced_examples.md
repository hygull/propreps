```python
In [1]: {frozenset("Python"), tuple("Golang")}
Out[1]: {('G', 'o', 'l', 'a', 'n', 'g'), frozenset({'P', 'h', 'n', 'o', 't', 'y'})}
```

```python
In [2]: {frozenset("Python"), tuple("Golang"), (1, 5, 7, 8, 9)}
Out[2]: 
{('G', 'o', 'l', 'a', 'n', 'g'),
 (1, 5, 7, 8, 9),
 frozenset({'P', 'h', 'n', 'o', 't', 'y'})}

In [3]: items = {frozenset("Python"), tuple("Golang"), (1, 5, 7, 8, 9)}

In [4]: for item in items:
   ...:     print("item ->", item)
   ...: 
item -> ('G', 'o', 'l', 'a', 'n', 'g')
item -> frozenset({'P', 't', 'n', 'h', 'y', 'o'})
item -> (1, 5, 7, 8, 9)

In [5]: for item in items:
   ...:     print(f"item -> {item}")
   ...: 
item -> ('G', 'o', 'l', 'a', 'n', 'g')
item -> frozenset({'P', 't', 'n', 'h', 'y', 'o'})
item -> (1, 5, 7, 8, 9)
```

```python
In [9]: frozenset([frozenset([2, 4, 10]), frozenset([3, 7, 9])])
Out[9]: frozenset({frozenset({3, 7, 9}), frozenset({2, 4, 10})})
```
