```python
In [1]: import re

In [2]: sentence = "One of my fav language is python and it is great!"

In [3]: re.sub(r"is", "was", sentence)
Out[3]: 'One of my fav language was python and it was great!'
```

```python
In [5]: print(sentence)
One of my fav language is python and it is great!

In [6]: sentence
Out[6]: 'One of my fav language is python and it is great!'

In [7]: re.split(r"\s", sentence)
Out[7]: 
['One',
 'of',
 'my',
 'fav',
 'language',
 'is',
 'python',
 'and',
 'it',
 'is',
 'great!']

In [8]: sentence2 = "One  of my fav language  is python  and it is     great!"

In [9]: sentence2
Out[9]: 'One  of my fav language  is python  and it is     great!'

In [10]: re.split(r"\s", sentence2)
Out[10]: 
['One',
 '',
 'of',
 'my',
 'fav',
 'language',
 '',
 'is',
 'python',
 '',
 'and',
 'it',
 'is',
 '',
 '',
 '',
 '',
 'great!']

In [11]: re.split(r"\s+", sentence2)
Out[11]: 
['One',
 'of',
 'my',
 'fav',
 'language',
 'is',
 'python',
 'and',
 'it',
 'is',
 'great!']
 ```

 ```python
 In [12]: sentence3 = "Here1goes2the417usage987examples1789related76to123python!"

In [13]: words = re.split(r"\d+", sentence3)

In [14]: print(words)
['Here', 'goes', 'the', 'usage', 'examples', 'related', 'to', 'python!']
```

```python
In [15]: words = re.split(r"^\d+$", sentence3)

In [16]: print(words)
['Here1goes2the417usage987examples1789related76to123python!']
```

```python

In [17]: str_numbers = re.split(r"[a-z]+", sentence3)

In [18]: print(str_numbers)
['H', '1', '2', '417', '987', '1789', '76', '123', '!']

In [19]: str_numbers = re.split(r"[a-zA-Z!]+", sentence3)

In [20]: print(str_numbers)
['', '1', '2', '417', '987', '1789', '76', '123', '']

In [21]: str_numbers = [int(str_number) for str_number in str_numbers if str_number]

In [22]: print(str_numbers)
[1, 2, 417, 987, 1789, 76, 123]
```
