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