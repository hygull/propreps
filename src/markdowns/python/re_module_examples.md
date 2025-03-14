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