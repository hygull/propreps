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

```python
In [10]: hem = Person(first_name="Hemkesh", last_name="Agrawani", age=30)

In [11]: hem.first_name
Out[11]: 'Hemkesh'

In [12]: hem.last_name
Out[12]: 'Agrawani'

In [13]: hem.age
Out[13]: 30

In [14]: hem.languages
Out[14]: []

In [15]: hem.languages.append("C")

In [16]: hem.languages
Out[16]: ['C']

In [17]: hem.languages.extend(["C++", "Python"])

In [18]: hem.languages
Out[18]: ['C', 'C++', 'Python']
```

