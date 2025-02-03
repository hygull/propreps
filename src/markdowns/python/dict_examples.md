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