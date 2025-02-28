```python
In [1]: first_name = "Rishikesh"

In [2]: for ch in first_name:
   ...:     print(ch)
   ...: 
R
i
s
h
i
k
e
s
h

In [3]: for ch in first_name[::-1]:
   ...:     print(ch)
   ...: 
h
s
e
k
i
h
s
i
R

In [4]: first_name
Out[4]: 'Rishikesh'

In [5]: first_name[:]
Out[5]: 'Rishikesh'

In [6]: first_name[::-1]
Out[6]: 'hsekihsiR'
```

```python
In [7]: i = 0

In [8]: while i < len(first_name):
   ...:     print(first_name[i])
   ...:     i += 1
   ...: 
R
i
s
h
i
k
e
s
h

In [9]: i = len(first_name) - 1

In [10]: while i > -1:
    ...:     print(first_name[i])
    ...:     i -= 1
    ...: 
h
s
e
k
i
h
s
i
R

In [11]: 
```

```python
In [11]: "Rishikesh"[:1]
Out[11]: 'R'

In [12]: "Rishikesh"[::-1]
Out[12]: 'hsekihsiR'

In [13]: "Rishikesh"[::-1] "Hemkesh"[::-1]
  File "<ipython-input-13-a4fadb83eb6b>", line 1
    "Rishikesh"[::-1] "Hemkesh"[::-1]
                              ^
SyntaxError: invalid syntax


In [14]: "Rishikesh"[::-1] + "Hemkesh"[::-1]
Out[14]: 'hsekihsiRhsekmeH'

In [15]: "Rishikesh" "Hemkesh"
Out[15]: 'RishikeshHemkesh'
```

```python
In [16]: "Rishikesh" "Hemkesh" * 5
Out[16]: 'RishikeshHemkeshRishikeshHemkeshRishikeshHemkeshRishikeshHemkeshRishikeshHemkesh'

In [18]: "Rishikesh" * len("Hemkesh")
Out[18]: 'RishikeshRishikeshRishikeshRishikeshRishikeshRishikeshRishikesh'
```


```python
In [1]: "Rishkesh"[0]
Out[1]: 'R'

In [2]: "Rishkesh"[1]
Out[2]: 'i'

In [3]: "Rishkesh"[-1]
Out[3]: 'h'

In [4]: "Rishkesh"[-2]
Out[4]: 's'

In [5]: "Rishkesh"[-3]
Out[5]: 'e'

In [6]: "Rishkesh"[-4]
Out[6]: 'k'

In [7]: first_name = "Rishikesh"

In [8]: first_name[-1]
Out[8]: 'h'

In [9]: first_name[5]
Out[9]: 'k'

In [10]: first_name[2]
Out[10]: 's'

In [11]: first_name[0]
Out[11]: 'R'

In [12]: first_name[:-3]
Out[12]: 'Rishik'

In [13]: first_name[:-4]
Out[13]: 'Rishi'

In [14]: first_name[-3:-4]
Out[14]: ''

In [15]: first_name[-3:-5]
Out[15]: ''

In [16]: first_name[-3: -1]
Out[16]: 'es'
```

```python
In [17]: "Hello" 'programmers' '!'[-1]
Out[17]: '!'

In [18]: "Hello" 'programmers' '!'[0]
Out[18]: 'H'

In [19]: "Hello" 'programmers' '!'
Out[19]: 'Helloprogrammers!'
```


```python
In [19]: "Hello" 'programmers' '!'
Out[19]: 'Helloprogrammers!'

In [20]: "Hello" + 'programmers' + '!'
Out[20]: 'Helloprogrammers!'

In [21]: f"{'Hello' + 'programmers' + '!'}"
Out[21]: 'Helloprogrammers!'
```

```python
In [22]: "%s" % ("Rishikesh")
Out[22]: 'Rishikesh'

In [23]: "%s %s %d %s" % ("Rishikesh", "is", 32, "years old")
Out[23]: 'Rishikesh is 32 years old'
```

```python
In [24]: "{first_name} is {age} years old".format(first_name="Rishikesh", age=10)
Out[24]: 'Rishikesh is 10 years old'
```

```python
In [1]: "Ram"[0]
Out[1]: 'R'

In [2]: "Ram"[-1]
Out[2]: 'm'

In [3]: "Ram"[1]
Out[3]: 'a'

In [4]: "Ram"[:1]
Out[4]: 'R'

In [5]: "Ram"[0:1]
Out[5]: 'R'

In [6]: "Ram"[0:-11]
Out[6]: ''

In [8]: "Ram"[0:-1]
Out[8]: 'Ra'

In [9]: "Ram"[0:-2]
Out[9]: 'R'

In [10]: "Ram"[0:-3]
Out[10]: ''
```

```python
In [11]: "Shiva" "Ram" "Krishna"
Out[11]: 'ShivaRamKrishna'

In [13]: "Shiva"[:-1] + "Ram"[:-1] + "Krishna"[:-1]
Out[13]: 'ShivRaKrishn'
```

```python
In [14]: "Lord Shiva Jee"
Out[14]: 'Lord Shiva Jee'

In [15]: "Lord Shiva Jee"[-2:-1]
Out[15]: 'e'

In [16]: "Lord Shiva Jee"[-3:-1]
Out[16]: 'Je'

In [17]: "Lord Shiva Jee"[-3:]
Out[17]: 'Jee'

In [18]: "Lord Shiva Jee"[-3:0]
Out[18]: ''

In [19]: "Lord Shiva Jee"[0:-3]
Out[19]: 'Lord Shiva '

In [20]: "Lord Shiva Jee"[0:-2]
Out[20]: 'Lord Shiva J'

In [21]: "Lord Shiva Jee"[0:-1]
Out[21]: 'Lord Shiva Je'

In [22]: "Lord Shiva Jee"[0:]
Out[22]: 'Lord Shiva Jee'
```

```python
In [4]: "-------------".split()
Out[4]: ['-------------']

In [5]: "-------------".split("-")
Out[5]: ['', '', '', '', '', '', '', '', '', '', '', '', '', '']

In [6]: "+".join("-------------".split("-"))
Out[6]: '+++++++++++++'
```

```python
In [13]: def update_name(name):
    ...:     return f"{name}, you are awe!"
    ...: 

In [14]: map(update_name, ["Rishikesh", "Hemkesh", "Malinikesh"])
Out[14]: <map at 0x7fc5a8e18668>

In [15]: list(map(update_name, ["Rishikesh", "Hemkesh", "Malinikesh"]))
Out[15]: 
['Rishikesh, you are awe!',
 'Hemkesh, you are awe!',
 'Malinikesh, you are awe!']
```

```python
In [16]: pd.DataFrame(map(update_name, ["Rishikesh", "Hemkesh", "Malinikesh"]), columns=["message"])
Out[16]: 
                    message
0   Rishikesh, you are awe!
1     Hemkesh, you are awe!
2  Malinikesh, you are awe!
```
