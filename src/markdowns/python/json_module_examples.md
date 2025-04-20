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

```python
In [68]: pretty_details = json.dumps(details, indent=4, separators=(" #", " -> "))

In [69]: print(pretty_details)
{
    "first_name" -> "Rishikesh" #
    "last_name" -> "Agrawani" #
    "age" -> 32
}

In [70]: type(pretty_details)
Out[70]: str

In [71]: pretty_details[0]
Out[71]: '{'

In [72]: pretty_details[1]
Out[72]: '\n'

In [73]: pretty_details[2]
Out[73]: ' '

In [74]: pretty_details[3]
Out[74]: ' '

In [75]: pretty_details[4]
Out[75]: ' '

In [76]: pretty_details[5]
Out[76]: ' '

In [77]: pretty_details[6]
Out[77]: '"'

In [78]: pretty_details[7]
Out[78]: 'f'
```

```python
In [79]: details = json.loads(pretty_details)
---------------------------------------------------------------------------
JSONDecodeError                           Traceback (most recent call last)
<ipython-input-79-0f72a6cfc541> in <module>
----> 1 details = json.loads(pretty_details)

/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/__init__.py in loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)
    352             parse_int is None and parse_float is None and
    353             parse_constant is None and object_pairs_hook is None and not kw):
--> 354         return _default_decoder.decode(s)
    355     if cls is None:
    356         cls = JSONDecoder

/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/decoder.py in decode(self, s, _w)
    337 
    338         """
--> 339         obj, end = self.raw_decode(s, idx=_w(s, 0).end())
    340         end = _w(s, end).end()
    341         if end != len(s):

/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/decoder.py in raw_decode(self, s, idx)
    353         """
    354         try:
--> 355             obj, end = self.scan_once(s, idx)
    356         except StopIteration as err:
    357             raise JSONDecodeError("Expecting value", s, err.value) from None

JSONDecodeError: Expecting ':' delimiter: line 2 column 18 (char 19)
```

```python

In [82]: details = json.loads(pretty_details.replace(" #", " ,").replace(" -> ", " : "))

In [83]: print(details)
{'first_name': 'Rishikesh', 'last_name': 'Agrawani', 'age': 32}

In [84]: type(details)
Out[84]: dict

In [85]: details["first_name"]
Out[85]: 'Rishikesh'
```