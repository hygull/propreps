### collections - Counter

```shell
In [1]: from collections import Counter

In [2]: c = Counter([1, 4, 5, 6, 7, 1, 9 + 1, 90, 10, 0 + 1, 8 - 2, 45 * 2])

In [3]: c
Out[3]: Counter({1: 3, 4: 1, 5: 1, 6: 2, 7: 1, 10: 2, 90: 2})

In [4]: for key, value in c.items():
   ...:     print(key, '->', value)
   ...: 
1 -> 3
4 -> 1
5 -> 1
6 -> 2
7 -> 1
10 -> 2
90 -> 2

In [5]: for key, value in c.items():
   ...:     print(f"{key} -> {value}")
   ...: 
   ...: 
1 -> 3
4 -> 1
5 -> 1
6 -> 2
7 -> 1
10 -> 2
90 -> 2
```

### collections - OrderedDict

```shell
In [1]: from collections import OrderedDict

In [2]: d = OrderedDict()

In [3]: d["fullname"] = "Rishikesh Agrawani"

In [4]: d["brother_fullname"] = "Hemkesh Agrawani"

In [5]: d["sister_fullname"] = "Malinikesh Agrawani"

In [6]: d
Out[6]: 
OrderedDict([('fullname', 'Rishikesh Agrawani'),
             ('brother_fullname', 'Hemkesh Agrawani'),
             ('sister_fullname', 'Malinikesh Agrawani')])

In [7]: d["age"] = 32

In [8]: d["brother_age"] = 30

In [9]: d["sister_age"] = 28

In [10]: d
Out[10]: 
OrderedDict([('fullname', 'Rishikesh Agrawani'),
             ('brother_fullname', 'Hemkesh Agrawani'),
             ('sister_fullname', 'Malinikesh Agrawani'),
             ('age', 32),
             ('brother_age', 30),
             ('sister_age', 28)])

In [11]: for key, value in d.items():
    ...:     print(f"{key} -> {value}")
    ...: 
fullname -> Rishikesh Agrawani
brother_fullname -> Hemkesh Agrawani
sister_fullname -> Malinikesh Agrawani
age -> 32
brother_age -> 30
sister_age -> 28

In [12]: for key, value in d.items():
    ...:     print(f"{key:<20} -> {value:<20}")
    ...: 
fullname             -> Rishikesh Agrawani  
brother_fullname     -> Hemkesh Agrawani    
sister_fullname      -> Malinikesh Agrawani 
age                  -> 32                  
brother_age          -> 30                  
sister_age           -> 28
```