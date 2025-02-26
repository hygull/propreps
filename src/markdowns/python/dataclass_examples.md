```python
In [1]: from typing import List

In [2]: from dataclasses import dataclass, field

In [3]: @dataclass
   ...: class Person:
   ...:     first_name: str
   ...:     last_name: str
   ...:     age: int
   ...:     languages: List[str] = field(default_factory=list) # list is callable here
   ...: 

In [4]: rishi = Person(first_name="Rishikesh", last_name="Agrawani", age=32, languages=["Python"])

In [5]: rishi.first_name
Out[5]: 'Rishikesh'

In [6]: rishi.last_name
Out[6]: 'Agrawani'

In [7]: rishi.age
Out[7]: 32

In [8]: rishi.languages
Out[8]: ['Python']
```

