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

# collections - deque

```shell
In [5]: from collections import deque

In [6]: fruits_dq = deque(["Apple", "Banana", "Pine apple", "Papaya", "Grape"])

In [7]: fruits_dq
Out[7]: deque(['Apple', 'Banana', 'Pine apple', 'Papaya', 'Grape'])

In [8]: fruits_dq.append("Gooseberry")

In [9]: fruits_dq
Out[9]: deque(['Apple', 'Banana', 'Pine apple', 'Papaya', 'Grape', 'Gooseberry'])

In [10]: fruits_dq.appendleft("Gooseberry")

In [11]: fruits_dq
Out[11]: 
deque(['Gooseberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry'])

In [12]: fruits_dq.popleft("Gooseberry")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-730e8c36affb> in <module>
----> 1 fruits_dq.popleft("Gooseberry")

TypeError: popleft() takes no arguments (1 given)

In [13]: fruits_dq.popleft()
Out[13]: 'Gooseberry'

In [14]: fruits_dq
Out[14]: deque(['Apple', 'Banana', 'Pine apple', 'Papaya', 'Grape', 'Gooseberry'])

In [15]: fruits_dq.appendleft("Strawberry")

In [16]: fruits_dq
Out[16]: 
deque(['Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry'])

In [17]: fruits_dq.extend(["Mango", "Kiwi"])

In [18]: fruits_dq
Out[18]: 
deque(['Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi'])

In [19]: fruits_dq.extendleft(["Raspberry", "Blueberry"])

In [20]: fruits_dq
Out[20]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi'])

In [21]: fruits_dq.append("Kiwi")

In [22]: fruits_dq
Out[22]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi',
       'Kiwi'])

In [23]: fruits_dq.remove("Kiwi")

In [24]: fruits_dq
Out[24]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi'])

In [25]: fruits_dq.extend(["Plum", "Peach", "Banana"])

In [26]: fruits_dq
Out[26]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi',
       'Plum',
       'Peach',
       'Banana'])

In [27]: fruits_dq.remove("Banana")

In [28]: fruits_dq
Out[28]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi',
       'Plum',
       'Peach',
       'Banana'])

In [29]: fruits_dq.index("Apple")
Out[29]: 3

In [30]: fruits_dq[3]
Out[30]: 'Apple'

In [31]: for fruit_name in fruits_dq:
    ...:     print(fruit_name)
    ...: 
Blueberry
Raspberry
Strawberry
Apple
Pine apple
Papaya
Grape
Gooseberry
Mango
Kiwi
Plum
Peach
Banana
```


# collections - defaultdict

```shell
In [1]: from collections import defaultdict

In [2]: fruits_dict = defaultdict(int)

In [3]: fruits_dict["Apple"] += 5

In [4]: fruits_dict
Out[4]: defaultdict(int, {'Apple': 5})

In [5]: fruits_dict["Banana"]
Out[5]: 0

In [6]: fruits_dict
Out[6]: defaultdict(int, {'Apple': 5, 'Banana': 0})

In [7]: fruits_dict["Banana"] += 6

In [8]: fruits_dict
Out[8]: defaultdict(int, {'Apple': 5, 'Banana': 6})

In [9]: for key, value in fruits_dict.items():
   ...:     print(f"{key} => {value}")
   ...: 
Apple => 5
Banana => 6

In [10]: for key, value in fruits_dict.items():
    ...:     print(f"{key:<8} => {value:>8}")
    ...: 
Apple    =>        5
Banana   =>        6

In [11]: fruits_dict.items()
Out[11]: dict_items([('Apple', 5), ('Banana', 6)])

In [12]: fruits_dict.keys()
Out[12]: dict_keys(['Apple', 'Banana'])

In [13]: fruits_dict.values()
Out[13]: dict_values([5, 6])

In [14]: fruits_dict.clear()

In [15]: fruits_dict
Out[15]: defaultdict(int, {})
```

```shell
In [25]: numbers_dict = defaultdict(list)

In [26]: numbers_dict
Out[26]: defaultdict(list, {})

In [27]: numbers_dict["even_numbers"].extend([2, 4, 6, 8, 10])

In [28]: numbers_dict
Out[28]: defaultdict(list, {'even_numbers': [2, 4, 6, 8, 10]})

In [29]: numbers_dict["odd_numbers"].extend([1, 3, 5, 7, 9])

In [30]: numbers_dict
Out[30]: 
defaultdict(list,
            {'even_numbers': [2, 4, 6, 8, 10], 'odd_numbers': [1, 3, 5, 7, 9]})
```

```shell
In [31]: books_dict = defaultdict(tuple)

In [32]: books_dict
Out[32]: defaultdict(tuple, {})

In [33]: books_dict["programming_books"] += ("Let us C", "Core Java")

In [34]: books_dict
Out[34]: defaultdict(tuple, {'programming_books': ('Let us C', 'Core Java')})

In [35]: books_dict["poetry_books"].extend(("Mongli and Wolf", "Ghost with Angels"))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-35-190f65902710> in <module>
----> 1 books_dict["poetry_books"].extend(("Mongli and Wolf", "Ghost with Angels"))

AttributeError: 'tuple' object has no attribute 'extend'

In [36]: books_dict
Out[36]: 
defaultdict(tuple,
            {'programming_books': ('Let us C', 'Core Java'),
             'poetry_books': ()})
```