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

### Use of `\t`

```python
In [16]: print("Rishi\tkesh")
Rishi kesh
```

### Use of `\r`

```python
In [17]: print("Rishi\rkesh")
keshi

In [18]: print("Rishi\rkesh\r")
keshi

In [19]: print("Rishikesh\r")
Rishikesh

In [20]: print("Rishikesh\rAgr")
Agrhikesh
```

### Use of `\f`

```python
In [21]: print("Rishike\fsh")
Rishike
       sh

In [22]: print("Rishike\fsh\fis\fgoing\fto\fdo")
Rishike
       sh
         is
           going
                to
                  do

In [23]: print("Rishikesh\fis\fgoing\fto\fdo\fthe\fdeployment!")
Rishikesh
         is
           going
                to
                  do
                    the
                       deployment!
```

```python
In [24]: "A\bishi\thj"
Out[24]: 'A\x08ishi\thj'

In [25]: print("A\bishi\thj")
ishi  hj

In [26]: "Rishi\f\fThis is"
Out[26]: 'Rishi\x0c\x0cThis is'

In [27]: print("Rishi\f\fThis is")
Rishi

     This is

In [28]: print("Rishi\f\f\fThis is")
Rishi


     This is

In [30]: print("Rishi\fThis is")
Rishi
     This is
````

```python
In [31]: print("Ui\fth\n")
Ui
  th


In [32]: print("Ui\fth\nK")
Ui
  th
K

In [33]: print("Ui\f\ntn")
Ui

tn

In [34]: print("Ui\f\rtn")
Ui
tn
```