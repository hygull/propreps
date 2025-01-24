### DataFrame's loc (Label based indexing)

```python
In [1]: import pandas as pd

In [2]: persons_persons_df.= pd.DataFrame({
   ...:     "first_name": ["Malinikesh", "Hemkesh", "Rishikesh"],
   ...:     "last_name": ["Agrawani", "Agrawani", "Agrawani"],
   ...:     "age": [28, 30, 32],
   ...: })

In [3]: persons_df
Out[3]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agrawani   32

In [4]: persons_persons_df.loc[0] # 1st row
Out[4]: 
first_name    Malinikesh
last_name       Agrawani
age                   28
Name: 0, dtype: object

In [5]: persons_persons_df.loc[:, "first_name"] # 1st column
Out[5]: 
0    Malinikesh
1       Hemkesh
2     Rishikesh
Name: first_name, dtype: object

In [6]: persons_persons_df.loc[:, ["first_name", "age"]] # 2 columns
Out[6]: 
   first_name  age
0  Malinikesh   28
1     Hemkesh   30
2   Rishikesh   32

In [7]: persons_persons_df.loc[[1, 2], ["first_name", "age"]] # 2 columns, 2 rows
Out[7]: 
  first_name  age
1    Hemkesh   30
2  Rishikesh   32

In [8]: persons_persons_df.loc[[1, 2], "first_name":"age"]
Out[8]: 
  first_name last_name  age
1    Hemkesh  Agrawani   30
2  Rishikesh  Agrawani   32

In [9]: persons_persons_df.loc[[1, 2], "first_name":"last_name"]
Out[9]: 
  first_name last_name
1    Hemkesh  Agrawani
2  Rishikesh  Agrawani

In [10]: persons_persons_df.loc[0:1, "first_name":"last_name"]
Out[10]: 
   first_name last_name
0  Malinikesh  Agrawani
1     Hemkesh  Agrawani

In [11]: persons_persons_df.loc[0:, "first_name":"last_name"]
Out[11]: 
   first_name last_name
0  Malinikesh  Agrawani
1     Hemkesh  Agrawani
2   Rishikesh  Agrawani

In [12]: persons_persons_df.loc[0:, "first_name":]
Out[12]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agrawani   32

In [13]: 
```


### DataFrame's iloc (Integer-location based indexing)

```bash
In [14]: persons_persons_df.iloc[0]
Out[14]: 
first_name    Malinikesh
last_name       Agrawani
age                   28
Name: 0, dtype: object

In [15]: persons_persons_df.iloc[0:]
Out[15]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agrawani   32

In [16]: persons_persons_df.iloc[0:1]
Out[16]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28

In [17]: persons_persons_df.iloc[0:2]
Out[17]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30

In [18]: persons_persons_df.iloc[0:3]
Out[18]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agrawani   32

In [19]: persons_persons_df.iloc[0:3, 0:1]
Out[19]: 
   first_name
0  Malinikesh
1     Hemkesh
2   Rishikesh

In [20]: persons_persons_df.iloc[0:3, 0:2]
Out[20]: 
   first_name last_name
0  Malinikesh  Agrawani
1     Hemkesh  Agrawani
2   Rishikesh  Agrawani

In [21]: persons_persons_df.iloc[0:3, "first_name"]
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexing.py in _has_valid_tuple(self, key)
    701             try:
...
...
...
ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types

In [22]: 
```

### Filtering examples

```python
In [21]: persons_df
Out[21]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agrawani   32

In [22]: persons_persons_df.loc[persons_persons_df."age"] > 30]
Out[22]: 
  first_name last_name  age
2  Rishikesh  Agrawani   32

In [23]: persons_persons_df.loc[persons_persons_df."age"] == 30]
Out[23]: 
  first_name last_name  age
1    Hemkesh  Agrawani   30

In [24]: persons_persons_df.loc[persons_persons_df."age"] < 30]
Out[24]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28

In [25]: persons_persons_df.loc[persons_persons_df."age"] <= 30]
Out[25]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
```

```python
In [27]: persons_persons_df.loc[(persons_persons_df."age"] <= 30) & (persons_persons_df."first_name"].isin(["Malinikesh  Agrawani", "Hemkesh  Agrawani"]))]
Out[27]: 
Empty DataFrame
Columns: [first_name, last_name, age]
Index: []

In [28]: persons_persons_df.loc[(persons_persons_df."age"] <= 30) & (persons_persons_df."first_name"].isin(["Malinikesh", "Hemkesh"]))]
Out[28]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
```


```python
In [29]: persons_persons_df.loc[persons_persons_df."age"] <= 30]
Out[29]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30

In [30]: persons_persons_df.loc[persons_persons_df."age"] == 30, "first_name"] = "Hem"

In [31]: persons_df
Out[31]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1         Hem  Agrawani   30
2   Rishikesh  Agrawani   32

In [32]: persons_persons_df.loc[persons_persons_df."age"] == 32, "first_name"] = "Rishi"

In [33]: persons_persons_df.loc[persons_persons_df."age"] == 28, "first_name"] = "Malini"

In [34]: persons_df
Out[34]: 
  first_name last_name  age
0     Malini  Agrawani   28
1        Hem  Agrawani   30
2      Rishi  Agrawani   32
```

### Index and columns
```python
In [35]: persons_persons_df.index
Out[35]: RangeIndex(start=0, stop=3, step=1)

In [36]: persons_persons_df.index.tolist()
Out[36]: [0, 1, 2]

In [37]: persons_persons_df.columns.tolist()
Out[37]: ['first_name', 'last_name', 'age']

In [38]: persons_persons_df.columns
Out[38]: Index(['first_name', 'last_name', 'age'], dtype='object')
```

```python
In [39]: persons_df
Out[39]: 
  first_name last_name  age
0     Malini  Agrawani   28
1        Hem  Agrawani   30
2      Rishi  Agrawani   32

In [40]: persons_persons_df."village"] = "Risgaon"

In [41]: persons_df
Out[41]: 
  first_name last_name  age  village
0     Malini  Agrawani   28  Risgaon
1        Hem  Agrawani   30  Risgaon
2      Rishi  Agrawani   32  Risgaon

In [42]: persons_persons_df."age"].gt(30)
Out[42]: 
0    False
1    False
2     True
Name: age, dtype: bool

In [44]: persons_persons_df."age"].lt(30)
Out[44]: 
0     True
1    False
2    False
Name: age, dtype: bool

In [45]: persons_persons_df."age"].gt(30).sum()
Out[45]: 1

In [46]: persons_persons_df."age"].lt(30).sum()
Out[46]: 1

In [47]: persons_persons_df."age"].gt(25).sum()
Out[47]: 3
```

```python
In [1]: persons_df.= pd.DataFrame(columns=["column1", "column2"])

In [2]: df
Out[2]: 
Empty DataFrame
Columns: [column1, column2]
Index: []

In [3]: persons_df.empty
Out[3]: True

In [4]: persons_df.shape
Out[4]: (0, 2)

In [5]: persons_df.shape[0]
Out[5]: 0
```

```python
In [1]: import pandas as pd

In [2]: data = {
   ...:     "name": "Alice",
   ...:     "age": 30,
   ...:     "address": {
   ...:         "city": "Wonderland",
   ...:         "zip": "12345"
   ...:     }
   ...: }

In [3]: df = pd.json_normalize(data)

In [4]: df
Out[4]: 
    name  age address.city address.zip
0  Alice   30   Wonderland       12345

In [5]: 

In [5]: data = {
   ...:     "school": "Springfield Elementary",
   ...:     "students": [
   ...:         {"name": "Bart", "grade": 4},
   ...:         {"name": "Lisa", "grade": 3}
   ...:     ]
   ...: }

In [6]: df = pd.json_normalize(data, record_path='students')

In [7]: df
Out[7]: 
   name  grade
0  Bart      4
1  Lisa      3

In [8]: df = pd.json_normalize(data, record_path='students', meta='school')

In [9]: df
Out[9]: 
   name  grade                  school
0  Bart      4  Springfield Elementary
1  Lisa      3  Springfield Elementary

In [10]: 

In [10]: {
    ...:   "name": "Alice",
    ...:   "age": 30,
    ...:   "address": {
    ...:     "city": "Wonderland",
    ...:     "zip": "12345"
    ...:   }
    ...: }
Out[10]: {'name': 'Alice', 'age': 30, 'address': {'city': 'Wonderland', 'zip': '12345'}}

In [11]: data = {
    ...:     "name": "Alice",
    ...:     "age": 30,
    ...:     "address": {
    ...:         "city": "Wonderland",
    ...:         "zip": "12345"
    ...:     }
    ...: }

In [12]: df = pd.json_normalize(data)

In [13]: df
Out[13]: 
    name  age address.city address.zip
0  Alice   30   Wonderland       12345
```


```python
In [16]: data = {
    ...:     "company": "Tech Co",
    ...:     "employees": [
    ...:         {
    ...:             "name": "John",
    ...:             "role": "Developer",
    ...:             "projects": [
    ...:                 {"title": "Website Revamp", "hours": 120},
    ...:                 {"title": "App Development", "hours": 200}
    ...:             ]
    ...:         },
    ...:         {
    ...:             "name": "Jane",
    ...:             "role": "Designer",
    ...:             "projects": [
    ...:                 {"title": "Logo Design", "hours": 80}
    ...:             ]
    ...:         }
    ...:     ]
    ...: }

In [17]: df = pd.json_normalize(
    ...:     data,
    ...:     record_path=['employees', 'projects'],
    ...:     meta=[['employees', 'name'], ['employees', 'role'], 'company']
    ...: )

In [18]: df
Out[18]: 
             title  hours employees.name employees.role  company
0   Website Revamp    120           John      Developer  Tech Co
1  App Development    200           John      Developer  Tech Co
2      Logo Design     80           Jane       Designer  Tech Co

In [19]: 

```