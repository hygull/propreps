```python
In [1]: print("-+-" * 80)
-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-

In [2]: print("-+-" * 40)
-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-

In [3]: for i in range(10):
   ...:     print(i)
   ...: 
0
1
2
3
4
5
6
7
8
9

In [4]: for i in range(10):
   ...:     print(i ** 2)
   ...: 
0
1
4
9
16
25
36
49
64
81

In [5]: for i in range(10):
   ...:     print(i, '->', i ** 2)
   ...: 
0 -> 0
1 -> 1
2 -> 4
3 -> 9
4 -> 16
5 -> 25
6 -> 36
7 -> 49
8 -> 64
9 -> 81
```

```bash
In [6]: numbers = range(1, 11)

In [7]: for number in numbers:
   ...:     print("Number: ", number)
   ...: 
Number:  1
Number:  2
Number:  3
Number:  4
Number:  5
Number:  6
Number:  7
Number:  8
Number:  9
Number:  10

In [8]: for number in numbers:
   ...:     print("Number: ", number ** 2 \
   ...:     )
   ...: 
Number:  1
Number:  4
Number:  9
Number:  16
Number:  25
Number:  36
Number:  49
Number:  64
Number:  81
Number:  100
```

```bash
In [12]: for number in numbers:
    ...:     print(
    ...:         "Number: ", number
    ...:         ** 2
    ...:     )
    ...: 
Number:  1
Number:  4
Number:  9
Number:  16
Number:  25
Number:  36
Number:  49
Number:  64
Number:  81
Number:  100
```