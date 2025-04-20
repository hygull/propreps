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

```json
In [61]: import json

In [62]: details = {"first_name": "Rishikesh", "last_name": "Agrawani", "age": 32}

In [63]: print(details)
{'first_name': 'Rishikesh', 'last_name': 'Agrawani', 'age': 32}

In [64]: pretty_details = json.dumps(details, indent=4)

In [65]: print(type(pretty_details))
<class 'str'>

In [66]: pretty_details
Out[66]: '{\n    "first_name": "Rishikesh",\n    "last_name": "Agrawani",\n    "age": 32\n}'

In [67]: print(pretty_details)
{
    "first_name": "Rishikesh",
    "last_name": "Agrawani",
    "age": 32
}
```