```python
In [1]: person = {
   ...:     "first_name": "Rishikesh",
   ...:     "last_name": "Agrawani",
   ...:     "age": 32,
   ...:     "programming_languages": ["C", "C++", "Python", "Java"],
   ...:     "address": {
   ...:         "city": "Raipur",
   ...:         "state": "Chhattisgarh"
   ...:     }
   ...: }

In [2]: person
Out[2]: 
{'first_name': 'Rishikesh',
 'last_name': 'Agrawani',
 'age': 32,
 'programming_languages': ['C', 'C++', 'Python', 'Java'],
 'address': {'city': 'Raipur', 'state': 'Chhattisgarh'}}

In [3]: import json

In [4]: print(json.dumps(person, indent=4))
{
    "first_name": "Rishikesh",
    "last_name": "Agrawani",
    "age": 32,
    "programming_languages": [
        "C",
        "C++",
        "Python",
        "Java"
    ],
    "address": {
        "city": "Raipur",
        "state": "Chhattisgarh"
    }
}
```


```python
In [8]: print(json.dumps(person, indent=4, separators=(";", "->")))
{
    "first_name"->"Rishikesh";
    "last_name"->"Agrawani";
    "age"->32;
    "programming_languages"->[
        "C";
        "C++";
        "Python";
        "Java"
    ];
    "address"->{
        "city"->"Raipur";
        "state"->"Chhattisgarh"
    }
}

In [9]: print(json.dumps(person, indent=4, separators=("; ", "-> ")))
{
    "first_name"-> "Rishikesh"; 
    "last_name"-> "Agrawani"; 
    "age"-> 32; 
    "programming_languages"-> [
        "C"; 
        "C++"; 
        "Python"; 
        "Java"
    ]; 
    "address"-> {
        "city"-> "Raipur"; 
        "state"-> "Chhattisgarh"
    }
}

In [10]: print(json.dumps(person, indent=4, separators=(": ", ", ")))
{
    "first_name", "Rishikesh": 
    "last_name", "Agrawani": 
    "age", 32: 
    "programming_languages", [
        "C": 
        "C++": 
        "Python": 
        "Java"
    ]: 
    "address", {
        "city", "Raipur": 
        "state", "Chhattisgarh"
    }
}
```