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

