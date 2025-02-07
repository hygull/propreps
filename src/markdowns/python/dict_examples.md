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