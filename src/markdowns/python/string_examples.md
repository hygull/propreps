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
In [13]: def get_message(name):
    ...:     return f"{name}, you are awe!"
    ...: 

In [14]: map(get_message, ["Rishikesh", "Hemkesh", "Malinikesh"])
Out[14]: <map at 0x7fc5a8e18668>

In [15]: list(map(get_message, ["Rishikesh", "Hemkesh", "Malinikesh"]))
Out[15]: 
['Rishikesh, you are awe!',
 'Hemkesh, you are awe!',
 'Malinikesh, you are awe!']
```

```python
In [16]: pd.DataFrame(map(get_message, ["Rishikesh", "Hemkesh", "Malinikesh"]), columns=["message"])
Out[16]: 
                    message
0   Rishikesh, you are awe!
1     Hemkesh, you are awe!
2  Malinikesh, you are awe!
```

```python
In [17]: "(+)".replace("(", "[").replace(")", "]")
Out[17]: '[+]'

In [18]: "(+)".replace("(", "[").replace(")", "]").split("+")
Out[18]: ['[', ']']
```

```python
In [20]: "abcdefabc".strip("a")
Out[20]: 'bcdefabc'

In [21]: "aaaaabcdefabc".strip("a")
Out[21]: 'bcdefabc'

In [22]: "aaaaaybcdefabcxaaaaaaaa".strip("a")
Out[22]: 'ybcdefabcx'
```

```python
In [23]: "aaaaaybcdefabcxaaaaaaaa".lstrip("a")
Out[23]: 'ybcdefabcxaaaaaaaa'

In [24]: "aaaaaybcdefabcxaaaaaaaa".rstrip("a")
Out[24]: 'aaaaaybcdefabcx'
```

```python
In [26]: "a" * 2
Out[26]: 'aa'

In [27]: "a" * 5
Out[27]: 'aaaaa'

In [28]: "a" * 10
Out[28]: 'aaaaaaaaaa'
```

```python
In [29]: "python->" * 5
Out[29]: 'python->python->python->python->python->'
```

```python
In [1]: s = "+-+-+-+-+-+-+-+-"

In [2]: s.split("-")
Out[2]: ['+', '+', '+', '+', '+', '+', '+', '+', '']

In [3]: s.split("+")
Out[3]: ['', '-', '-', '-', '-', '-', '-', '-', '-']
```

```python
In [4]: s
Out[4]: '+-+-+-+-+-+-+-+-'

In [7]: s[:-1]
Out[7]: '+-+-+-+-+-+-+-+'

In [8]: s[-1:]
Out[8]: '-'
```

```python
In [1]: "AbcXyz".index("A") + 1
Out[1]: 1

In [2]: "AbcXyz".index("A")
Out[2]: 0

In [3]: "AbcXyz".index("X") + 3
Out[3]: 6

In [4]: "AbcXyz".index("A")
Out[4]: 0

In [5]: "AbcXyz".index("X")
Out[5]: 3
```

```python
In [6]: "Python"[: -2]
Out[6]: 'Pyth'

In [7]: "Python"[: -1]
Out[7]: 'Pytho'

In [8]: "Python"[: -1] + "nest"[:]
Out[8]: 'Pythonest'

In [9]: "Python"[: -1] + "nest"[1:2]
Out[9]: 'Pythoe'

In [10]: "Python"[: -1] + "nest"[0:1]
Out[10]: 'Python'
```

```python
In [11]: id("Python"[0])
Out[11]: 4357474784

In [12]: "Python"[0]
Out[12]: 'P'

In [13]: id("Python"[0])
Out[13]: 4357474784

In [14]: id("Python")
Out[14]: 4357096560
```

```python
In [2]: "3.12.1".split(".")
Out[2]: ['3', '12', '1']

In [3]: [int(number) for number in "3.12.1".split(".")]
Out[3]: [3, 12, 1]

In [4]: list(map(lambda number: int(number), "3.12.1".split(".")))
Out[4]: [3, 12, 1]
```

```python
In [5]: def get_number(number):
   ...:     return int(number)
   ...: 

In [6]: list(map(get_number, "3.12.1".split(".")))
Out[6]: [3, 12, 1]
```

```python

In [7]: numbers = []

In [8]: for number_as_str in "3.12.1".split("."):
   ...:     numbers.append(int(number_as_str))
   ...: 

In [9]: numbers
Out[9]: [3, 12, 1]
```

```python
In [1]: string  = "ABC-XYZ--PQR---MNO"

In [2]: string
Out[2]: 'ABC-XYZ--PQR---MNO'

In [3]: string.split("-")
Out[3]: ['ABC', 'XYZ', '', 'PQR', '', '', 'MNO']

In [4]: [word for word in string.split("-") if word.strip()]
Out[4]: ['ABC', 'XYZ', 'PQR', 'MNO']

In [5]: [word for word in string.split("-") if word]
Out[5]: ['ABC', 'XYZ', 'PQR', 'MNO']

In [6]: import re

In [7]: re.split(r"[\-]+", string)
Out[7]: ['ABC', 'XYZ', 'PQR', 'MNO']
```

```python
In [1]: "NAVRATRI-2025"
Out[1]: 'NAVRATRI-2025'

In [2]: " NAVRATRI-2025 "
Out[2]: ' NAVRATRI-2025 '

In [3]: " NAVRATRI-2025 ".strip()
Out[3]: 'NAVRATRI-2025'

In [4]: " NAVRATRI-2025 ".strip().split('-')
Out[4]: ['NAVRATRI', '2025']

In [5]: " NAVRATRI-2025 ".strip().split()
Out[5]: ['NAVRATRI-2025']

In [6]: " NAVRATRI-2025 ".strip().split('-')[0]
Out[6]: 'NAVRATRI'

In [7]: " NAVRATRI-2025 ".strip().split('-')[1]
Out[7]: '2025'

In [8]: int(" NAVRATRI-2025 ".strip().split('-')[1])
Out[8]: 2025
```

```python
In [1]: "<+>".split()
Out[1]: ['<+>']

In [2]: "<+>".split("+")
Out[2]: ['<', '>']

In [3]: "<+>".split("+")[0]
Out[3]: '<'

In [4]: "<+>".split("+")[1]
Out[4]: '>'

In [5]: "1010011101010001010101010111100010011010101010110010101111".split("0")
Out[5]: 
['1',
 '1',
 '',
 '111',
 '1',
 '1',
 '',
 '',
 '1',
 '1',
 '1',
 '1',
 '1',
 '1111',
 '',
 '',
 '1',
 '',
 '11',
 '1',
 '1',
 '1',
 '1',
 '11',
 '',
 '1',
 '1',
 '1111']

In [6]: "1010011101010001010101010111100010011010101010110010101111".split("1")
Out[6]: 
['',
 '0',
 '00',
 '',
 '',
 '0',
 '0',
 '000',
 '0',
 '0',
 '0',
 '0',
 '0',
 '',
 '',
 '',
 '000',
 '00',
 '',
 '0',
 '0',
 '0',
 '0',
 '0',
 '',
 '00',
 '0',
 '0',
 '',
 '',
 '',
 '']
```

```python
In [7]: zeros = "1010011101010001010101010111100010011010101010110010101111".split("1")

In [8]: print(zeros)
['', '0', '00', '', '', '0', '0', '000', '0', '0', '0', '0', '0', '', '', '', '000', '00', '', '0', '0', '0', '0', '0', '', '00', '0', '0', '', '', '', '']

In [9]: zeros = [int(zero) for zero in zeros if zero]

In [10]: print(zeros)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

In [11]: ones = "1010011101010001010101010111100010011010101010110010101111".split("0")

In [12]: print(ones)
['1', '1', '', '111', '1', '1', '', '', '1', '1', '1', '1', '1', '1111', '', '', '1', '', '11', '1', '1', '1', '1', '11', '', '1', '1', '1111']

In [13]: ones = [int(one) for one in ones if one]

In [14]: print(ones)
[1, 1, 111, 1, 1, 1, 1, 1, 1, 1, 1111, 1, 11, 1, 1, 1, 1, 11, 1, 1, 1111]
```

```python
In [15]: "<.>".replace("<", "{").replace(">", "}")
Out[15]: '{.}'

In [16]: "<A>".replace("<", "{").replace(">", "}")
Out[16]: '{A}'

In [17]: "<'A'>".replace("<", "{").replace(">", "}")
Out[17]: "{'A'}"
```