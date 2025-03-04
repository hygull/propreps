### collections - Counter

```python
In [1]: from collections import Counter

In [2]: c = Counter([1, 4, 5, 6, 7, 1, 9 + 1, 90, 10, 0 + 1, 8 - 2, 45 * 2])

In [3]: c
Out[3]: Counter({1: 3, 4: 1, 5: 1, 6: 2, 7: 1, 10: 2, 90: 2})

In [4]: for key, value in c.items():
   ...:     print(key, '->', value)
   ...: 
1 -> 3
4 -> 1
5 -> 1
6 -> 2
7 -> 1
10 -> 2
90 -> 2

In [5]: for key, value in c.items():
   ...:     print(f"{key} -> {value}")
   ...: 
   ...: 
1 -> 3
4 -> 1
5 -> 1
6 -> 2
7 -> 1
10 -> 2
90 -> 2
```

### collections - OrderedDict

```python
In [1]: from collections import OrderedDict

In [2]: d = OrderedDict()

In [3]: d["fullname"] = "Rishikesh Agrawani"

In [4]: d["brother_fullname"] = "Hemkesh Agrawani"

In [5]: d["sister_fullname"] = "Malinikesh Agrawani"

In [6]: d
Out[6]: 
OrderedDict([('fullname', 'Rishikesh Agrawani'),
             ('brother_fullname', 'Hemkesh Agrawani'),
             ('sister_fullname', 'Malinikesh Agrawani')])

In [7]: d["age"] = 32

In [8]: d["brother_age"] = 30

In [9]: d["sister_age"] = 28

In [10]: d
Out[10]: 
OrderedDict([('fullname', 'Rishikesh Agrawani'),
             ('brother_fullname', 'Hemkesh Agrawani'),
             ('sister_fullname', 'Malinikesh Agrawani'),
             ('age', 32),
             ('brother_age', 30),
             ('sister_age', 28)])

In [11]: for key, value in d.items():
    ...:     print(f"{key} -> {value}")
    ...: 
fullname -> Rishikesh Agrawani
brother_fullname -> Hemkesh Agrawani
sister_fullname -> Malinikesh Agrawani
age -> 32
brother_age -> 30
sister_age -> 28

In [12]: for key, value in d.items():
    ...:     print(f"{key:<20} -> {value:<20}")
    ...: 
fullname             -> Rishikesh Agrawani  
brother_fullname     -> Hemkesh Agrawani    
sister_fullname      -> Malinikesh Agrawani 
age                  -> 32                  
brother_age          -> 30                  
sister_age           -> 28
```

# collections - deque

```python
In [5]: from collections import deque

In [6]: fruits_dq = deque(["Apple", "Banana", "Pine apple", "Papaya", "Grape"])

In [7]: fruits_dq
Out[7]: deque(['Apple', 'Banana', 'Pine apple', 'Papaya', 'Grape'])

In [8]: fruits_dq.append("Gooseberry")

In [9]: fruits_dq
Out[9]: deque(['Apple', 'Banana', 'Pine apple', 'Papaya', 'Grape', 'Gooseberry'])

In [10]: fruits_dq.appendleft("Gooseberry")

In [11]: fruits_dq
Out[11]: 
deque(['Gooseberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry'])

In [12]: fruits_dq.popleft("Gooseberry")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-730e8c36affb> in <module>
----> 1 fruits_dq.popleft("Gooseberry")

TypeError: popleft() takes no arguments (1 given)

In [13]: fruits_dq.popleft()
Out[13]: 'Gooseberry'

In [14]: fruits_dq
Out[14]: deque(['Apple', 'Banana', 'Pine apple', 'Papaya', 'Grape', 'Gooseberry'])

In [15]: fruits_dq.appendleft("Strawberry")

In [16]: fruits_dq
Out[16]: 
deque(['Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry'])

In [17]: fruits_dq.extend(["Mango", "Kiwi"])

In [18]: fruits_dq
Out[18]: 
deque(['Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi'])

In [19]: fruits_dq.extendleft(["Raspberry", "Blueberry"])

In [20]: fruits_dq
Out[20]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi'])

In [21]: fruits_dq.append("Kiwi")

In [22]: fruits_dq
Out[22]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi',
       'Kiwi'])

In [23]: fruits_dq.remove("Kiwi")

In [24]: fruits_dq
Out[24]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi'])

In [25]: fruits_dq.extend(["Plum", "Peach", "Banana"])

In [26]: fruits_dq
Out[26]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Banana',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi',
       'Plum',
       'Peach',
       'Banana'])

In [27]: fruits_dq.remove("Banana")

In [28]: fruits_dq
Out[28]: 
deque(['Blueberry',
       'Raspberry',
       'Strawberry',
       'Apple',
       'Pine apple',
       'Papaya',
       'Grape',
       'Gooseberry',
       'Mango',
       'Kiwi',
       'Plum',
       'Peach',
       'Banana'])

In [29]: fruits_dq.index("Apple")
Out[29]: 3

In [30]: fruits_dq[3]
Out[30]: 'Apple'

In [31]: for fruit_name in fruits_dq:
    ...:     print(fruit_name)
    ...: 
Blueberry
Raspberry
Strawberry
Apple
Pine apple
Papaya
Grape
Gooseberry
Mango
Kiwi
Plum
Peach
Banana
```


# collections - defaultdict

```python
In [1]: from collections import defaultdict

In [2]: fruits_dict = defaultdict(int)

In [3]: fruits_dict["Apple"] += 5

In [4]: fruits_dict
Out[4]: defaultdict(int, {'Apple': 5})

In [5]: fruits_dict["Banana"]
Out[5]: 0

In [6]: fruits_dict
Out[6]: defaultdict(int, {'Apple': 5, 'Banana': 0})

In [7]: fruits_dict["Banana"] += 6

In [8]: fruits_dict
Out[8]: defaultdict(int, {'Apple': 5, 'Banana': 6})

In [9]: for key, value in fruits_dict.items():
   ...:     print(f"{key} => {value}")
   ...: 
Apple => 5
Banana => 6

In [10]: for key, value in fruits_dict.items():
    ...:     print(f"{key:<8} => {value:>8}")
    ...: 
Apple    =>        5
Banana   =>        6

In [11]: fruits_dict.items()
Out[11]: dict_items([('Apple', 5), ('Banana', 6)])

In [12]: fruits_dict.keys()
Out[12]: dict_keys(['Apple', 'Banana'])

In [13]: fruits_dict.values()
Out[13]: dict_values([5, 6])

In [14]: fruits_dict.clear()

In [15]: fruits_dict
Out[15]: defaultdict(int, {})
```

```python
In [25]: numbers_dict = defaultdict(list)

In [26]: numbers_dict
Out[26]: defaultdict(list, {})

In [27]: numbers_dict["even_numbers"].extend([2, 4, 6, 8, 10])

In [28]: numbers_dict
Out[28]: defaultdict(list, {'even_numbers': [2, 4, 6, 8, 10]})

In [29]: numbers_dict["odd_numbers"].extend([1, 3, 5, 7, 9])

In [30]: numbers_dict
Out[30]: 
defaultdict(list,
            {'even_numbers': [2, 4, 6, 8, 10], 'odd_numbers': [1, 3, 5, 7, 9]})
```

```python
In [31]: books_dict = defaultdict(tuple)

In [32]: books_dict
Out[32]: defaultdict(tuple, {})

In [33]: books_dict["programming_books"] += ("Let us C", "Core Java")

In [34]: books_dict
Out[34]: defaultdict(tuple, {'programming_books': ('Let us C', 'Core Java')})

In [35]: books_dict["poetry_books"].extend(("Mongli and Wolf", "Ghost with Angels"))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-35-190f65902710> in <module>
----> 1 books_dict["poetry_books"].extend(("Mongli and Wolf", "Ghost with Angels"))

AttributeError: 'tuple' object has no attribute 'extend'

In [36]: books_dict
Out[36]: 
defaultdict(tuple,
            {'programming_books': ('Let us C', 'Core Java'),
             'poetry_books': ()})
```

```python
In [39]: class Person:
    ...:     def __init__(self, first_name, last_name, age):
    ...:         self.first_name = first_name
    ...:         self.last_name = last_name
    ...:         self.age = age
    ...: 
    ...:     def print_details(self):
    ...:         print(f"Full name: {self.first_name} {self.last_name}")
    ...:         print(f"Age: {self.age}")
    ...: 

In [40]: person1 = Person("Rishikesh", "Agrawani", 32)

In [41]: person1
Out[41]: <__main__.Person at 0x7fadc841cef0>

In [42]: person1.print_details()
Full name: Rishikesh Agrawani
Age: 32

In [43]: persons_dict = defaultdict(Person)

In [44]: persons_dict
Out[44]: defaultdict(__main__.Person, {})

In [45]: persons_dict["Rishikesh"].first_name
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-45-a0b5ecfd780d> in <module>
----> 1 persons_dict["Rishikesh"].first_name

TypeError: __init__() missing 3 required positional arguments: 'first_name', 'last_name', and 'age'

In [46]: persons_dict["Rishikesh"]("Hemkesh", "Agrawani", 30)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-46-3cc2f38f8e24> in <module>
----> 1 persons_dict["Rishikesh"]("Hemkesh", "Agrawani", 30)

TypeError: __init__() missing 3 required positional arguments: 'first_name', 'last_name', and 'age'

In [47]: class Person:
    ...:     def __init__(self, first_name=None, last_name=None, age=None):
    ...:         self.first_name = first_name
    ...:         self.last_name = last_name
    ...:         self.age = age
    ...: 
    ...:     def print_details(self):
    ...:         print(f"Full name: {self.first_name} {self.last_name}")
    ...:         print(f"Age: {self.age}")
    ...: 

In [48]: persons_dict["Rishikesh"]("Hemkesh", "Agrawani", 30)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-48-3cc2f38f8e24> in <module>
----> 1 persons_dict["Rishikesh"]("Hemkesh", "Agrawani", 30)

TypeError: __init__() missing 3 required positional arguments: 'first_name', 'last_name', and 'age'

In [49]: persons_dict = defaultdict(Person)

In [50]: persons_dict["Rishikesh"]
Out[50]: <__main__.Person at 0x7fade8ba6588>

In [51]: persons_dict["Rishikesh"].first_name

In [52]: print(persons_dict["Rishikesh"].first_name)
None

In [53]: persons_dict
Out[53]: 
defaultdict(__main__.Person,
            {'Rishikesh': <__main__.Person at 0x7fade8ba6588>})

In [54]: persons_dict["Hemkesh"].first_name = "Hemkesh"

In [55]: persons_dict["Hemkesh"].__dict__
Out[55]: {'first_name': 'Hemkesh', 'last_name': None, 'age': None}
```

# collections - namedtuple

```python
In [1]: from collections import namedtuple

In [2]: Person = namedtuple("Person", ["first_name", "last_name", "age"])

In [3]: Person
Out[3]: __main__.Person

In [4]: person = Person("Rishikesh", "Agrawani", 32)

In [5]: person[0]
Out[5]: 'Rishikesh'

In [6]: person[1]
Out[6]: 'Agrawani'

In [7]: person[2]
Out[7]: 32

In [8]: person[3]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-8-56d117fa3037> in <module>
----> 1 person[3]

IndexError: tuple index out of range

In [9]: person.first_name
Out[9]: 'Rishikesh'

In [10]: person.last_name
Out[10]: 'Agrawani'

In [11]: person.age
Out[11]: 32

In [12]: person
Out[12]: Person(first_name='Rishikesh', last_name='Agrawani', age=32)

In [13]: person_details = person

In [14]: for person_detail in person_details:
    ...:     print(person_detail)
    ...: 
Rishikesh
Agrawani
32

In [15]: person2 = Person("Hemkesh", "Agrawani", 30)

In [16]: person2
Out[16]: Person(first_name='Hemkesh', last_name='Agrawani', age=30)

In [17]: person + person2
Out[17]: ('Rishikesh', 'Agrawani', 32, 'Hemkesh', 'Agrawani', 30)

In [18]: combined_details = person + person2

In [19]: type(person)
Out[19]: __main__.Person

In [20]: type(person2)
Out[20]: __main__.Person

In [21]: type(combined_details)
Out[21]: tuple

In [22]: for combined_detail in combined_details:
    ...:     print(combined_detail)
    ...: 
Rishikesh
Agrawani
32
Hemkesh
Agrawani
30
```

# collections - ChainMap

```python
In [1]: from collections import ChainMap

In [2]: even_numbers = {2: "two", 4: "four", 8: "eight", 10: "ten"}

In [3]: even_numbers
Out[3]: {2: 'two', 4: 'four', 8: 'eight', 10: 'ten'}

In [4]: odd_numbers = {1: "one", 5: "five", 9: "nine", 11: "eleven"}

In [5]: odd_numbers
Out[5]: {1: 'one', 5: 'five', 9: 'nine', 11: 'eleven'}

In [6]: fav_numbers = {1 + 1: "two.2nd", 7+ 2: "nine.2nd"}

In [7]: chainmap = ChainMap(even_numbers, odd_numbers, fav_numbers)

In [8]: chainmap
Out[8]: ChainMap({2: 'two', 4: 'four', 8: 'eight', 10: 'ten'}, {1: 'one', 5: 'five', 9: 'nine', 11: 'eleven'}, {2: 'two.2nd', 9: 'nine.2nd'})

In [9]: chainmap[2]
Out[9]: 'two'

In [10]: chainmap[9]
Out[10]: 'nine'

In [11]: chainmap[10]
Out[11]: 'ten'

In [12]: 

In [12]: chainmap = ChainMap(fav_numbers, even_numbers, odd_numbers)

In [13]: chainmap[2]
Out[13]: 'two.2nd'

In [14]: chainmap[9]
Out[14]: 'nine.2nd'

In [15]: chainmap[10]
Out[15]: 'ten'

In [16]: 

In [16]: chainmap.new_child({12: "twelve", 14: "fourteen", 15: "fifteen"})
Out[16]: ChainMap({12: 'twelve', 14: 'fourteen', 15: 'fifteen'}, {2: 'two.2nd', 9: 'nine.2nd'}, {2: 'two', 4: 'four', 8: 'eight', 10: 'ten'}, {1: 'one', 5: 'five', 9: 'nine', 11: 'eleven'})

In [17]: chainmap
Out[17]: ChainMap({2: 'two.2nd', 9: 'nine.2nd'}, {2: 'two', 4: 'four', 8: 'eight', 10: 'ten'}, {1: 'one', 5: 'five', 9: 'nine', 11: 'eleven'})

In [18]: chainmap = chainmap.new_child({12: "twelve", 14: "fourteen", 15: "fifteen"})

In [19]: chainmap
Out[19]: ChainMap({12: 'twelve', 14: 'fourteen', 15: 'fifteen'}, {2: 'two.2nd', 9: 'nine.2nd'}, {2: 'two', 4: 'four', 8: 'eight', 10: 'ten'}, {1: 'one', 5: 'five', 9: 'nine', 11: 'eleven'})

In [20]: chainmap[11]
Out[20]: 'eleven'

In [21]: chainmap[12]
Out[21]: 'twelve'

In [22]: 

In [22]: for k, v in chainmap.items():
    ...:     print(k, v)
    ...: 
1 one
2 two.2nd
4 four
5 five
8 eight
9 nine.2nd
10 ten
11 eleven
12 twelve
14 fourteen
15 fifteen
```


```python
In [1]: import collections

In [2]: collections.Counter([1, 3, 5, 6, 8, 19, 1, 3, 5, 7, 90])
Out[2]: Counter({1: 2, 3: 2, 5: 2, 6: 1, 8: 1, 19: 1, 7: 1, 90: 1})

In [3]: numbers_dict = collections.Counter([1, 3, 5, 6, 8, 19, 1, 3, 5, 7, 90])

In [4]: for number, freq in numbers_dict.items():
   ...:     print(number, freq)
   ...: 
1 2
3 2
5 2
6 1
8 1
19 1
7 1
90 1

In [5]: for number, freq in numbers_dict.items():
   ...:     print(number, '->', freq)
   ...: 
1 -> 2
3 -> 2
5 -> 2
6 -> 1
8 -> 1
19 -> 1
7 -> 1
90 -> 1
```

