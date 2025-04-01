```python
In [1]: details = {
   ...:     "first_name": "Rishikesh",
   ...:     "last_name": "Agrawani",
   ...:     "age": 32,
   ...:     "relatives": {
   ...:         "brother": {
   ...:             "first_name": "Hemkesh",
   ...:             "last_name": "Agrawani",
   ...:             "age": 30
   ...:         },
   ...:         "sister": {
   ...:             "first_name": "Malinikesh",
   ...:             "last_name": "Agrawani",
   ...:             "age": 28
   ...:        }
   ...:    },
   ...:    "fav_books": ["Let us C", "Core Java", "C with classes"]
   ...: }

In [2]: details
Out[2]: 
{'first_name': 'Rishikesh',
 'last_name': 'Agrawani',
 'age': 32,
 'relatives': {'brother': {'first_name': 'Hemkesh',
   'last_name': 'Agrawani',
   'age': 30},
  'sister': {'first_name': 'Malinikesh', 'last_name': 'Agrawani', 'age': 28}},
 'fav_books': ['Let us C', 'Core Java', 'C with classes']}

In [3]: import json

In [4]: print(json.dumps(details, indent=4))
{
    "first_name": "Rishikesh",
    "last_name": "Agrawani",
    "age": 32,
    "relatives": {
        "brother": {
            "first_name": "Hemkesh",
            "last_name": "Agrawani",
            "age": 30
        },
        "sister": {
            "first_name": "Malinikesh",
            "last_name": "Agrawani",
            "age": 28
        }
    },
    "fav_books": [
        "Let us C",
        "Core Java",
        "C with classes"
    ]
}
```


```python
In [5]: for key, value in details.items():
   ...:     print(key, " => ", value)
   ...: 
first_name  =>  Rishikesh
last_name  =>  Agrawani
age  =>  32
relatives  =>  {'brother': {'first_name': 'Hemkesh', 'last_name': 'Agrawani', 'age': 30}, 'sister': {'first_name': 'Malinikesh', 'last_name': 'Agrawani', 'age': 28}}
fav_books  =>  ['Let us C', 'Core Java', 'C with classes']

In [6]: details["relatives"]
Out[6]: 
{'brother': {'first_name': 'Hemkesh', 'last_name': 'Agrawani', 'age': 30},
 'sister': {'first_name': 'Malinikesh', 'last_name': 'Agrawani', 'age': 28}}

In [7]: details["relatives"]["brother"]
Out[7]: {'first_name': 'Hemkesh', 'last_name': 'Agrawani', 'age': 30}

In [8]: details["relatives"]["brother"]["first_name"]
Out[8]: 'Hemkesh'

In [9]: details["relatives"]["brother"]["last_name"]
Out[9]: 'Agrawani'

In [10]: details["relatives"]["brother"]["age"]
Out[10]: 30

In [11]: for book in details["fav_books"]:
    ...:     print(book)
    ...: 
Let us C
Core Java
C with classes
```

```python
In [2]: details = {"first_name": "Rishikesh"}

In [3]: details
Out[3]: {'first_name': 'Rishikesh'}

In [4]: details.update({"last_name": "Agrawani", "age": 32})

In [5]: details
Out[5]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani', 'age': 32}

In [6]: details.values()
Out[6]: dict_values(['Rishikesh', 'Agrawani', 32])

In [7]: details.keys()
Out[7]: dict_keys(['first_name', 'last_name', 'age'])

In [8]: details.items()
Out[8]: dict_items([('first_name', 'Rishikesh'), ('last_name', 'Agrawani'), ('age', 32)])

In [10]: details.pop("age")
Out[10]: 32

In [11]: details
Out[11]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

In [12]: details.popitem()
Out[12]: ('last_name', 'Agrawani')

In [13]: details.popitem()
Out[13]: ('first_name', 'Rishikesh')

In [14]: details.setdefault("first_name")

In [15]: details
Out[15]: {'first_name': None}

In [16]: details.setdefault("first_name", "Rishikesh")

In [17]: details
Out[17]: {'first_name': None}

In [18]: details.setdefault("last_name", "Agrawani")
Out[18]: 'Agrawani'

In [19]: details
Out[19]: {'first_name': None, 'last_name': 'Agrawani'}

In [20]: details["first_name"] = "Rishikesh"

In [21]: details
Out[21]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}
```

```python
In [22]: details2 = details.copy()

In [23]: details2
Out[23]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

In [24]: details2["first_name"] = "Hemkesh"

In [25]: details2
Out[25]: {'first_name': 'Hemkesh', 'last_name': 'Agrawani'}

In [26]: details
Out[26]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

In [27]: details.get("first_name")
Out[27]: 'Rishikesh'

In [28]: details
Out[28]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

In [29]: details.fromkeys()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-29-41ddd82735ed> in <module>
----> 1 details.fromkeys()

TypeError: fromkeys expected at least 1 arguments, got 0

In [30]: details.fromkeys("4")
Out[30]: {'4': None}

In [31]: dict.fromkeys("4")
Out[31]: {'4': None}

In [32]: dict.fromkeys(4)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-32-706043d1721f> in <module>
----> 1 dict.fromkeys(4)

TypeError: 'int' object is not iterable

In [33]: dict.fromkeys(["rishikesh"])
Out[33]: {'rishikesh': None}

In [34]: dict.fromkeys("rishikesh")
Out[34]: {'r': None, 'i': None, 's': None, 'h': None, 'k': None, 'e': None}

In [35]: dict.fromkeys(["rishikesh", "hemkesh", "malinikesh"])
Out[35]: {'rishikesh': None, 'hemkesh': None, 'malinikesh': None}

In [36]: details
Out[36]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

In [37]: dict.fromkeys(details)
Out[37]: {'first_name': None, 'last_name': None}

In [38]: 
```

```bash
In [40]: dict.fromkeys(["age", "salary"], 0)
Out[40]: {'age': 0, 'salary': 0}

In [41]: {**dict.fromkeys(["age", "salary"], 0), **details}
Out[41]: {'age': 0, 'salary': 0, 'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

In [42]: dict(first_name="Rishikesh", last_name="Agrawani")
Out[42]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

In [43]: dict([("first_name", "Rishikesh"), ("last_name", "Agrawani")])
Out[43]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

In [45]: dict(**details)
Out[45]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

In [46]: {**details}
Out[46]: {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}
```

```python
In [1]: details = {"city": "Raipur", "state": "Chhattisgarh"}

In [2]: details
Out[2]: {'city': 'Raipur', 'state': 'Chhattisgarh'}

In [3]: details2 = details

In [4]: details["state"] = "CG"

In [5]: details
Out[5]: {'city': 'Raipur', 'state': 'CG'}

In [6]: details2
Out[6]: {'city': 'Raipur', 'state': 'CG'}

In [7]: # 2nd try

In [8]: details = {"city": "Raipur", "state": "Chhattisgarh"}

In [9]: details
Out[9]: {'city': 'Raipur', 'state': 'Chhattisgarh'}

In [10]: details2 = details.copy()

In [11]: details["state"] = "CG"

In [12]: details
Out[12]: {'city': 'Raipur', 'state': 'CG'}

In [13]: details2
Out[13]: {'city': 'Raipur', 'state': 'Chhattisgarh'}
```

```python
In [21]: details
Out[21]: {'city': 'Raipur', 'state': 'CG'}

In [22]: details.setdefault(9)

In [23]: details
Out[23]: {'city': 'Raipur', 'state': 'CG', 9: None}

In [24]: details.setdefault(9, 78)

In [25]: details
Out[25]: {'city': 'Raipur', 'state': 'CG', 9: None}

In [26]: details.setdefault(10, 78)
Out[26]: 78

In [27]: details
Out[27]: {'city': 'Raipur', 'state': 'CG', 9: None, 10: 78}
```

```python
In [29]: details
Out[29]: {'city': 'Raipur', 'state': 'CG', 9: None, 10: 78}

In [30]: details.clear()

In [31]: details
Out[31]: {}
```


```python
In [1]: numbers_vs_sum_map = {(1, 2): 3, (5, 4): 9, (56, 7): 90, (87, 5): 92}

In [2]: numbers_vs_sum_map
Out[2]: {(1, 2): 3, (5, 4): 9, (56, 7): 90, (87, 5): 92}

In [3]: for numbers_tup, _sum in numbers_vs_sum_map.items():
   ...:     print(numbers_tup, _sum)
   ...: 
(1, 2) 3
(5, 4) 9
(56, 7) 90
(87, 5) 92

In [4]: for numbers_tup, _sum in numbers_vs_sum_map.items():
   ...:     print(numbers_tup, _sum, sum(numbers_tup) == _sum)
   ...: 
(1, 2) 3 True
(5, 4) 9 True
(56, 7) 90 False
(87, 5) 92 True

In [5]: numbers_vs_sum_map = {numbers_tup: _sum for numbers_tup, _sum in numbers_vs_sum_map.items() if sum(numbers_tup) == _sum}

In [6]: numbers_vs_sum_map
Out[6]: {(1, 2): 3, (5, 4): 9, (87, 5): 92}
```

```python
In [6]: numbers_vs_sum_map
Out[6]: {(1, 2): 3, (5, 4): 9, (87, 5): 92}

In [7]: numbers_vs_sum_map.pop()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-9af81089ff3e> in <module>
----> 1 numbers_vs_sum_map.pop()

TypeError: pop expected at least 1 arguments, got 0
```

```python
In [8]: numbers_vs_sum_map.pop((87, 5))
Out[8]: 92


In [10]: numbers_vs_sum_map
Out[10]: {(1, 2): 3, (5, 4): 9}

In [11]: numbers_vs_sum_map.pop((5, 4))
Out[11]: 9

In [12]: numbers_vs_sum_map
Out[12]: {(1, 2): 3}

In [13]: numbers_vs_sum_map.pop((1, 2))
Out[13]: 3

In [14]: numbers_vs_sum_map
Out[14]: {}

In [15]: numbers_vs_sum_map == dict
Out[15]: False

In [16]: numbers_vs_sum_map == dict()
Out[16]: True

In [17]: numbers_vs_sum_map == {}
Out[17]: True

In [18]: type(numbers_vs_sum_map) == dict
Out[18]: True

In [19]: type(numbers_vs_sum_map) is dict
Out[19]: True

In [20]: 
```

```python
In [1]: details = {"city": "Raipur", "state": "Chhattisgarh"}

In [2]: details
Out[2]: {'city': 'Raipur', 'state': 'Chhattisgarh'}

In [3]: details["city"]
Out[3]: 'Raipur'

In [4]: details["city"] + details["state"]
Out[4]: 'RaipurChhattisgarh'
```

```python
In [5]: details["city"]  details["state"]
  Cell In[5], line 1
    details["city"]  details["state"]
                     ^
SyntaxError: invalid syntax
```

```python
In [6]: details["city"]
Out[6]: 'Raipur'

In [7]: details["state"]
Out[7]: 'Chhattisgarh'

In [8]: 'Raipur'  'Chhattisgarh'
Out[8]: 'RaipurChhattisgarh'

In [9]: details["city"] +  details["state"]
Out[9]: 'RaipurChhattisgarh'
```

```python
In [11]: details
Out[11]: {'city': 'Raipur', 'state': 'Chhattisgarh'}

In [12]: city = details["city"]

In [13]: city
Out[13]: 'Raipur'
```

```python
In [18]: city[:len(city)//2]
Out[18]: 'Rai'

In [19]: city[len(city)//2:]
Out[19]: 'pur'

In [20]: len(city)
Out[20]: 6

In [21]: state = details.get("state")

In [22]: state
Out[22]: 'Chhattisgarh'

In [23]: len(state)
Out[23]: 12

In [24]: state = state + "!"

In [25]: len(state)
Out[25]: 13

In [26]: state
Out[26]: 'Chhattisgarh!'

In [27]: state[: len(state) // 2]
Out[27]: 'Chhatt'

In [28]: state[len(state) // 2:]
Out[28]: 'isgarh!'

In [29]: 
```

```python
In [29]: "-*+)(&".split()
Out[29]: ['-*+)(&']

In [31]: list("-*+)(&")
Out[31]: ['-', '*', '+', ')', '(', '&']

In [32]: "".join(['-', '*', '+', ')', '(', '&'])
Out[32]: '-*+)(&'
```

```python
In [32]: "".join(['-', '*', '+', ')', '(', '&'])
Out[32]: '-*+)(&'

In [33]: "+".join(['-', '*', '+', ')', '(', '&'])
Out[33]: '-+*+++)+(+&'

In [34]: "<->".join(['-', '*', '+', ')', '(', '&'])
Out[34]: '-<->*<->+<->)<->(<->&'

In [35]: " <-> ".join(['-', '*', '+', ')', '(', '&'])
Out[35]: '- <-> * <-> + <-> ) <-> ( <-> &'
```

```python
In [36]: "RISHI".join("<>")
Out[36]: '<RISHI>'

In [37]: "RISHI".join("<>..")
Out[37]: '<RISHI>RISHI.RISHI.'
```

```python

In [38]: "RISHI".join("<>..").split(">")
Out[38]: ['<RISHI', 'RISHI.RISHI.']

In [39]: "RISHI".join("<>..").split(">")[0]
Out[39]: '<RISHI'

In [40]: "RISHI".join("<>..").split(">")[-1]
Out[40]: 'RISHI.RISHI.'
```


```python
In [3]: all_details = {"details": {}}

In [4]: all_details
Out[4]: {'details': {}}

In [5]: all_details.setdefault("details", {"first_name": "Rishikesh"})
Out[5]: {}

In [6]: all_details
Out[6]: {'details': {}}

In [7]: all_details.setdefault("details", {})["first_name"] = "Rishikesh"

In [8]: all_details
Out[8]: {'details': {'first_name': 'Rishikesh'}}

In [9]: all_details.setdefault("details")
Out[9]: {'first_name': 'Rishikesh'}

In [10]: all_details.setdefault("details")["last_name"] = "Agrawani"

In [11]: all_details.setdefault("details")["age"] = 32

In [12]: all_details
Out[12]: {'details': {'first_name': 'Rishikesh', 'last_name': 'Agrawani', 'age': 32}}

In [13]: import json

In [14]: print(json.dumps(all_details, indent=4))
{
    "details": {
        "first_name": "Rishikesh",
        "last_name": "Agrawani",
        "age": 32
    }
}
```

```python
In [15]: all_details = {}

In [16]: all_details
Out[16]: {}

In [17]: all_details.setdefault("details", {}).setdefault("first_name", "Agrawani")
Out[17]: 'Agrawani'

In [18]: all_details
Out[18]: {'details': {'first_name': 'Agrawani'}}

In [19]: all_details["details"]["first_name"] = "Rishikesh"

In [20]: all_details
Out[20]: {'details': {'first_name': 'Rishikesh'}}

In [21]: all_details.setdefault("details", {}).setdefault("last_name", "Agrawani")
Out[21]: 'Agrawani'

In [22]: all_details
Out[22]: {'details': {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}}
```

```python
In [1]: data = {"A": 12, "B": 89, "C": 90}

In [2]: c = data.pop("C")

In [3]: c
Out[3]: 90

In [4]: data
Out[4]: {'A': 12, 'B': 89}

In [5]: b = data.get("B")

In [6]: b
Out[6]: 89

In [7]: data
Out[7]: {'A': 12, 'B': 89}

In [8]: data.setdefault("C", 99)
Out[8]: 99

In [9]: data.setdefault("C", 99)
Out[9]: 99

In [10]: data
Out[10]: {'A': 12, 'B': 89, 'C': 99}
```

```python
In [12]: data.update({"D": data.pop("C") + 1})

In [13]: data
Out[13]: {'A': 12, 'B': 89, 'D': 100}
```

```python
In [16]: def f(B, A, D):
    ...:     print("D ->", D)
    ...:     print("B ->", B)
    ...:     print("A ->", A)
    ...: 

In [17]: f(**data)
D -> 100
B -> 89
A -> 12
```

```python
In [18]: def f(B, A, D, /):
    ...:     print("D ->", D)
    ...:     print("B ->", B)
    ...:     print("A ->", A)
    ...: 

In [19]: f(**data)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[19], line 1
----> 1 f(**data)

TypeError: f() got some positional-only arguments passed as keyword arguments: 'B, A, D'
```

```python
In [20]: f(10, 56, 77)
D -> 77
B -> 10
A -> 56

In [21]: f(*[11, 33, 103])
D -> 103
B -> 11
A -> 33

In [22]: f(*(12, 3, 13))
D -> 13
B -> 12
A -> 3

In [23]: f(*{14, 32, 9})
D -> 14
B -> 32
A -> 9
```


```python
In [1]: {"num1": 12, "num2": 89}
Out[1]: {'num1': 12, 'num2': 89}

In [2]: {"num1": 12, "num2": 89}.keys()
Out[2]: dict_keys(['num1', 'num2'])

In [3]: {"num1": 12, "num2": 89}.values()
Out[3]: dict_values([12, 89])

In [4]: tuple({"num1": 12, "num2": 89}.values())
Out[4]: (12, 89)

In [5]: set({"num1": 12, "num2": 89}.values())
Out[5]: {12, 89}

In [6]: list({"num1": 12, "num2": 89}.keys())
Out[6]: ['num1', 'num2']

In [7]: frozenset({"num1": 12, "num2": 89}.keys())
Out[7]: frozenset({'num1', 'num2'})

In [8]: set({"num1": 12, "num2": 89}.keys())
Out[8]: {'num1', 'num2'}

In [9]: tuple({"num1": 12, "num2": 89}.keys())
Out[9]: ('num1', 'num2')

In [10]: tuple({"num1": 12, "num2": 89}.keys()) + (1,)
Out[10]: ('num1', 'num2', 1)

In [11]: tuple({"num1": 12, "num2": 89}.keys()) + (1, 3)
Out[11]: ('num1', 'num2', 1, 3)

In [12]: tuple({"num1": 12, "num2": 89}.keys()) + (1, 5, 6)
Out[12]: ('num1', 'num2', 1, 5, 6)
```