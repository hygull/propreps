```python
In [1]: "\/\/\/\/\/\/\/\/\/\/\/\/"
Out[1]: '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/'

In [2]: s = "\/\/\/\/\/\/\/\/\/\/\/\/"

In [3]: s
Out[3]: '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/'

In [4]: print(s)
\/\/\/\/\/\/\/\/\/\/\/\/

In [5]: "\\"
Out[5]: '\\'
```

```python
In [6]: "\"
  File "<ipython-input-6-a16852ba415a>", line 1
    "\"
       ^
SyntaxError: EOL while scanning string literal

```

```python
In [7]: "\/"
Out[7]: '\\/'

In [8]: "\s"
Out[8]: '\\s'
```

### Use of `\n`
```python
In [9]: "Abc\nDef"
Out[9]: 'Abc\nDef'

In [10]: print("Abc\nDef")
Abc
Def
```

### Use of `\b`
```
In [11]: print("Abc\bDef")
AbDef

In [12]: print("Abc\b\bDef")
ADef

In [13]: print("Abc\b\b\bDef")
Def

In [14]: print("Abc\b\b\b\bDef")
Def

In [15]: print("Abc\b\b\b\b\bDef")
Def
```

