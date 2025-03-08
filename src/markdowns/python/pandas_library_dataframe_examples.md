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

```python
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


```python
In [1]: df = pd.DataFrame({"even_number": [2, 4, 8, 10, 22], "odd_number": [1, 5, 7, 19, 21]})

In [2]: df
Out[2]: 
   even_number  odd_number
0            2           1
1            4           5
2            8           7
3           10          19
4           22          21

In [3]: df.at[0, 'even_number']
Out[3]: 2

In [4]: df.at[0, 'even_number'] = 3

In [5]: df
Out[5]: 
   even_number  odd_number
0            3           1
1            4           5
2            8           7
3           10          19
4           22          21

In [6]: df.iat[0, 0]
Out[6]: 3

In [7]: df.iat[0, 0] = 55

In [8]: df
Out[8]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21

In [9]: df2 =  pd.DataFrame({"even_number": [28, 42, 90, 2, 44], "odd_number": [31, 25, 17, 1, 11]})

In [10]: df2
Out[10]: 
   even_number  odd_number
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11

In [11]: df.append(df2)
Out[11]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11

In [12]: df
Out[12]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21

In [13]: df3 = df.append(df2)

In [14]: df3
Out[14]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11

In [15]: df3.head()
Out[15]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21

In [16]: df3.head(n=2)
Out[16]: 
   even_number  odd_number
0           55           1
1            4           5

In [17]: df3.head(2)
Out[17]: 
   even_number  odd_number
0           55           1
1            4           5

In [18]: df3.head(3)
Out[18]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7

In [19]: df3.tail(3)
Out[19]: 
   even_number  odd_number
2           90          17
3            2           1
4           44          11

In [20]: df3.tail(2)
Out[20]: 
   even_number  odd_number
3            2           1
4           44          11

In [21]: df3.tail(n=2)
Out[21]: 
   even_number  odd_number
3            2           1
4           44          11

In [22]: df3.tail()
Out[22]: 
   even_number  odd_number
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11

In [23]: df3
Out[23]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11

In [24]: df3.reset_index()
Out[24]: 
   index  even_number  odd_number
0      0           55           1
1      1            4           5
2      2            8           7
3      3           10          19
4      4           22          21
5      0           28          31
6      1           42          25
7      2           90          17
8      3            2           1
9      4           44          11

In [25]: df3.reset_index(drop=True)
Out[25]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
5           28          31
6           42          25
7           90          17
8            2           1
9           44          11

In [26]: df3
Out[26]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11

In [27]: df3 = df3.reset_index(drop=True)

In [28]: # ...

In [29]: df3 = df.append(df2)

In [30]: df3
Out[30]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11

In [31]: df3.head(6)
Out[31]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
0           28          31

In [32]: df3.tail(6)
Out[32]: 
   even_number  odd_number
4           22          21
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11
```

```python
In [35]: df3
Out[35]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11

In [36]: df3.reset_index(drop=True)
Out[36]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
5           28          31
6           42          25
7           90          17
8            2           1
9           44          11

In [37]: df3
Out[37]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
0           28          31
1           42          25
2           90          17
3            2           1
4           44          11

In [38]: df3.reset_index(drop=True, inplace=True)

In [39]: df3
Out[39]: 
   even_number  odd_number
0           55           1
1            4           5
2            8           7
3           10          19
4           22          21
5           28          31
6           42          25
7           90          17
8            2           1
9           44          11
```

```python
In [44]: df = pd.DataFrame({"even_number": [np.nan, 4, np.nan, 10, 22], "odd_number": [1, 5, 7, 19, np.nan]})

In [45]: df
Out[45]: 
   even_number  odd_number
0          NaN         1.0
1          4.0         5.0
2          NaN         7.0
3         10.0        19.0
4         22.0         NaN

In [46]: df.fillna(0)
Out[46]: 
   even_number  odd_number
0          0.0         1.0
1          4.0         5.0
2          0.0         7.0
3         10.0        19.0
4         22.0         0.0

In [47]: df.fillna(11)
Out[47]: 
   even_number  odd_number
0         11.0         1.0
1          4.0         5.0
2         11.0         7.0
3         10.0        19.0
4         22.0        11.0

In [48]: df
Out[48]: 
   even_number  odd_number
0          NaN         1.0
1          4.0         5.0
2          NaN         7.0
3         10.0        19.0
4         22.0         NaN

In [49]: df.fillna(0, inplace=True)

In [50]: df
Out[50]: 
   even_number  odd_number
0          0.0         1.0
1          4.0         5.0
2          0.0         7.0
3         10.0        19.0
4         22.0         0.0

In [51]: 
```

```python
In [1]: df = pd.DataFrame({"odd_number": [1, 7, 9, 3], "even_number": [12, 14, 16, 20]})

In [2]: df
Out[2]: 
   odd_number  even_number
0           1           12
1           7           14
2           9           16
3           3           20

In [3]: df2 = pd.DataFrame({"odd_number": [1, 9, 3, 5], "even_number": [4, 10, 18, 22]})

In [4]: df2
Out[4]: 
   odd_number  even_number
0           1            4
1           9           10
2           3           18
3           5           22

In [5]: df3 = pd.DataFrame({"odd_number": [11, 99, 13, 55], "even_number": [48, 72, 88, 90]})

In [6]: df3
Out[6]: 
   odd_number  even_number
0          11           48
1          99           72
2          13           88
3          55           90

In [7]: df4 = pd.concat([df, df2, df3])

In [8]: df4
Out[8]: 
   odd_number  even_number
0           1           12
1           7           14
2           9           16
3           3           20
0           1            4
1           9           10
2           3           18
3           5           22
0          11           48
1          99           72
2          13           88
3          55           90

In [10]: df4 = pd.concat([df, df2, df3], ignore_index=True)

In [11]: df4
Out[11]: 
    odd_number  even_number
0            1           12
1            7           14
2            9           16
3            3           20
4            1            4
5            9           10
6            3           18
7            5           22
8           11           48
9           99           72
10          13           88
11          55           90

In [12]: 
```

```python
In [13]: df4 = pd.concat([df, df2, df3])

In [14]: df4
Out[14]: 
   odd_number  even_number
0           1           12
1           7           14
2           9           16
3           3           20
0           1            4
1           9           10
2           3           18
3           5           22
0          11           48
1          99           72
2          13           88
3          55           90

In [15]: df4.reset_index()
Out[15]: 
    index  odd_number  even_number
0       0           1           12
1       1           7           14
2       2           9           16
3       3           3           20
4       0           1            4
5       1           9           10
6       2           3           18
7       3           5           22
8       0          11           48
9       1          99           72
10      2          13           88
11      3          55           90

In [16]: df4.reset_index(drop=True)
Out[16]: 
    odd_number  even_number
0            1           12
1            7           14
2            9           16
3            3           20
4            1            4
5            9           10
6            3           18
7            5           22
8           11           48
9           99           72
10          13           88
11          55           90

In [17]: df4
Out[17]: 
   odd_number  even_number
0           1           12
1           7           14
2           9           16
3           3           20
0           1            4
1           9           10
2           3           18
3           5           22
0          11           48
1          99           72
2          13           88
3          55           90

In [18]: df4.reset_index(drop=True, inplace=True)

In [19]: df4
Out[19]: 
    odd_number  even_number
0            1           12
1            7           14
2            9           16
3            3           20
4            1            4
5            9           10
6            3           18
7            5           22
8           11           48
9           99           72
10          13           88
11          55           90

In [20]: 
```

```python
In [1]: import pandas as pd

In [2]: df =  pd.DataFrame({"even": [12, 0, 22, 56, 80], "odd": [3, 1, 9, 11, 15]})

In [3]: df
Out[3]: 
   even  odd
0    12    3
1     0    1
2    22    9
3    56   11
4    80   15

In [4]: df.set_index("even")
Out[4]: 
      odd
even     
12      3
0       1
22      9
56     11
80     15

In [5]: df.set_index("even")["odd"]
Out[5]: 
even
12     3
0      1
22     9
56    11
80    15
Name: odd, dtype: int64

In [6]: df.set_index("even")[["odd"]]
Out[6]: 
      odd
even     
12      3
0       1
22      9
56     11
80     15

In [7]: type(df.set_index("even")["odd"])
Out[7]: pandas.core.series.Series

In [8]: type(df.set_index("even")[["odd"]])
Out[8]: pandas.core.frame.DataFrame

In [9]: df.set_index("even")["odd"].to_dict()
Out[9]: {12: 3, 0: 1, 22: 9, 56: 11, 80: 15}

In [10]: df.set_index("even")[["odd"]].to_dict(orient="index")
Out[10]: 
{12: {'odd': 3},
 0: {'odd': 1},
 22: {'odd': 9},
 56: {'odd': 11},
 80: {'odd': 15}}

In [11]: df.set_index("even")[["odd"]].to_dict(orient="records")
Out[11]: [{'odd': 3}, {'odd': 1}, {'odd': 9}, {'odd': 11}, {'odd': 15}]
```

```python
In [13]: df["random"] = [1, 10,  5, 7, 8]

In [14]: df
Out[14]: 
   even  odd  random
0    12    3       1
1     0    1      10
2    22    9       5
3    56   11       7
4    80   15       8

In [15]: df.set_index(["even", "odd"])
Out[15]: 
          random
even odd        
12   3         1
0    1        10
22   9         5
56   11        7
80   15        8

In [16]: df.set_index(["odd", "even"])
Out[16]: 
          random
odd even        
3   12         1
1   0         10
9   22         5
11  56         7
15  80         8
```

```python
In [20]: new_df.loc[(3, 12)]
Out[20]: 
random    1
Name: (3, 12), dtype: int64

In [21]: new_df.loc[(3, 12), "random"]
Out[21]: 1

In [22]: new_df.loc[(3, 12), "random"]
```

```python
In [22]: new_df
Out[22]: 
          random
odd even        
3   12         1
1   0         10
9   22         5
11  56         7
15  80         8

In [23]: new_df.loc[3]
Out[23]: 
      random
even        
12         1

In [24]: new_df.loc[11]
Out[24]: 
      random
even        
56         7
```

```python
In [25]: new_df.xs(3, level="odd")
Out[25]: 
      random
even        
12         1

In [26]: new_df.xs(22, level="even")
Out[26]: 
     random
odd        
9         5     
```

```python
In [12]: df
Out[12]: 
   even  odd
0    12    3
1     0    1
2    22    9
3    56   11
4    80   15

In [13]: df.nlargest(3, columns=["even", "odd"])
Out[13]: 
   even  odd
4    80   15
3    56   11
2    22    9

In [14]: df.nlargest(3, columns=["even", "odd"])
Out[14]: 
   even  odd
4    80   15
3    56   11
2    22    9

In [15]: df =  pd.DataFrame({"even": [12, 0, 22, 56, 80], "odd": [84, 1, 90, 2, 80]})

In [16]: df
Out[16]: 
   even  odd
0    12   84
1     0    1
2    22   90
3    56    2
4    80   80

In [17]: df.nlargest(3, columns=["even", "odd"])
Out[17]: 
   even  odd
4    80   80
3    56    2
2    22   90

In [18]: df =  pd.DataFrame({"even": [12, 0, 22, 56, 80], "odd": [84, 1, 90, 2, 99]})

In [19]: df
Out[19]: 
   even  odd
0    12   84
1     0    1
2    22   90
3    56    2
4    80   99

In [20]: df.nlargest(3, columns=["even", "odd"])
Out[20]: 
   even  odd
4    80   99
3    56    2
2    22   90

In [21]: df.nlargest(3, columns=["odd", "even"])
Out[21]: 
   even  odd
4    80   99
2    22   90
0    12   84

In [22]: df =  pd.DataFrame({"even": [12, 0, 22, 56, 80, 1, 3], "odd": [84, 1, 90, 2, 99, 3, 99]})

In [23]: df
Out[23]: 
   even  odd
0    12   84
1     0    1
2    22   90
3    56    2
4    80   99
5     1    3
6     3   99

In [24]: df.nlargest(3, columns=["odd", "even"])
Out[24]: 
   even  odd
4    80   99
6     3   99
2    22   90

In [25]: df =  pd.DataFrame({"even": [12, 0, 22, 56, 3, 1, 80], "odd": [84, 1, 90, 2, 99, 3, 99]})

In [26]: df
Out[26]: 
   even  odd
0    12   84
1     0    1
2    22   90
3    56    2
4     3   99
5     1    3
6    80   99

In [27]: df.nlargest(3, columns=["odd", "even"])
Out[27]: 
   even  odd
6    80   99
4     3   99
2    22   90
```

```python
In [1]: df =  pd.DataFrame({"even": [12, 0, 22, 56, 3, 1, 80], "odd": [84, 1, 90, 2, 99, 3, 99]})

In [2]: df
Out[2]: 
   even  odd
0    12   84
1     0    1
2    22   90
3    56    2
4     3   99
5     1    3
6    80   99

In [3]: df.head()
Out[3]: 
   even  odd
0    12   84
1     0    1
2    22   90
3    56    2
4     3   99

In [4]: df.head(6)
Out[4]: 
   even  odd
0    12   84
1     0    1
2    22   90
3    56    2
4     3   99
5     1    3

In [5]: df.head(n=6)
Out[5]: 
   even  odd
0    12   84
1     0    1
2    22   90
3    56    2
4     3   99
5     1    3

In [6]: df.head(n=5)
Out[6]: 
   even  odd
0    12   84
1     0    1
2    22   90
3    56    2
4     3   99
```

```python
In [9]: df =  pd.DataFrame({"even": [12, 0, 22, 56, 3, 1, 80], "odd": [84, 1, 90, 2, 99, 3, 99], "group": ["A", "C", "A", "B", "B", "A", "C"]})

In [10]: df
Out[10]: 
   even  odd group
0    12   84     A
1     0    1     C
2    22   90     A
3    56    2     B
4     3   99     B
5     1    3     A
6    80   99     C

In [11]: df.groupby("group").agg({"even": "sum", "odd": "mean"})
Out[11]: 
       even   odd
group            
A        35  59.0
B        59  50.5
C        80  50.0

In [12]: df.groupby("group").agg({"even": "sum"})
Out[12]: 
       even
group      
A        35
B        59
C        80

In [13]: df.groupby("group").agg({"odd": "mean"})
Out[13]: 
        odd
group      
A      59.0
B      50.5
C      50.0
```

```python
In [15]: odd_mean_df
Out[15]: 
        odd
group      
A      59.0
B      50.5
C      50.0

In [16]: odd_mean_df.loc["A", "odd"]
Out[16]: 59.0

In [17]: odd_mean_df.iloc[0, 0]
Out[17]: 59.0

In [18]: odd_mean_df.iloc[0]
Out[18]: 
odd    59.0
Name: A, dtype: float64

In [20]: odd_mean_df.loc["A"]
Out[20]: 
odd    59.0
Name: A, dtype: float64
```

```python
In [1]: df = pd.DataFrame({"even": [2, 6, 90, 10, 44], "odd": [1, 5, 9, 19, 27]})

In [2]: df
Out[2]: 
   even  odd
0     2    1
1     6    5
2    90    9
3    10   19
4    44   27

In [3]: df.keys()
Out[3]: Index(['even', 'odd'], dtype='object')

In [4]: df.columns
Out[4]: Index(['even', 'odd'], dtype='object')

In [5]: df.items()
Out[5]: <generator object DataFrame.items at 0x7fc980d50e60>

In [6]: for item in df.items():
   ...:     print(item)
   ...: 
('even', 0     2
1     6
2    90
3    10
4    44
Name: even, dtype: int64)
('odd', 0     1
1     5
2     9
3    19
4    27
Name: odd, dtype: int64)

In [7]: for item in df.items():
   ...:     print(item[0])
   ...: 
even
odd

In [8]: for item in df.items():
   ...:     print(item[1])
   ...: 
0     2
1     6
2    90
3    10
4    44
Name: even, dtype: int64
0     1
1     5
2     9
3    19
4    27
Name: odd, dtype: int64

In [9]: for item in df.items():
   ...:     print(type(item[1]))
   ...: 
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
```

```python
In [10]: for i, row in df.iterrows():
    ...:     print(i)
    ...: 
0
1
2
3
4

In [11]: for i, row in df.iterrows():
    ...:     print(row)
    ...: 
even    2
odd     1
Name: 0, dtype: int64
even    6
odd     5
Name: 1, dtype: int64
even    90
odd      9
Name: 2, dtype: int64
even    10
odd     19
Name: 3, dtype: int64
even    44
odd     27
Name: 4, dtype: int64

In [12]: for i, row in df.iterrows():
    ...:     print(row.index)
    ...: 
Index(['even', 'odd'], dtype='object')
Index(['even', 'odd'], dtype='object')
Index(['even', 'odd'], dtype='object')
Index(['even', 'odd'], dtype='object')
Index(['even', 'odd'], dtype='object')

In [13]: for i, row in df.iterrows():
    ...:     print(row["even"])
    ...: 
2
6
90
10
44

In [14]: for i, row in df.iterrows():
    ...:     print(row["odd"])
    ...: 
1
5
9
19
27

In [15]: for i, row in df.iterrows():
    ...:     print(row.odd)
    ...: 
1
5
9
19
27

In [16]: for i, row in df.iterrows():
    ...:     print(row.even)
    ...: 
2
6
90
10
44


In [18]: for tup in df.itertuples():
    ...:     print(tup)
    ...: 
Pandas(Index=0, even=2, odd=1)
Pandas(Index=1, even=6, odd=5)
Pandas(Index=2, even=90, odd=9)
Pandas(Index=3, even=10, odd=19)
Pandas(Index=4, even=44, odd=27)

In [19]: for tup in df.itertuples():
    ...:     print(type(tup))
    ...: 
<class 'pandas.core.frame.Pandas'>
<class 'pandas.core.frame.Pandas'>
<class 'pandas.core.frame.Pandas'>
<class 'pandas.core.frame.Pandas'>
<class 'pandas.core.frame.Pandas'>

In [20]: for tup in df.itertuples():
    ...:     print(tup.Index)
    ...: 
0
1
2
3
4

In [21]: for tup in df.itertuples():
    ...:     print(tup.even)
    ...: 
2
6
90
10
44

In [22]: for tup in df.itertuples():
    ...:     print(tup.odd)
    ...: 
1
5
9
19
27

In [23]: for tup in df.itertuples():
    ...:     print(tup)
    ...: 
Pandas(Index=0, even=2, odd=1)
Pandas(Index=1, even=6, odd=5)
Pandas(Index=2, even=90, odd=9)
Pandas(Index=3, even=10, odd=19)
Pandas(Index=4, even=44, odd=27)

In [24]: for tup in df.itertuples(index=False):
    ...:     print(tup)
    ...: 
Pandas(even=2, odd=1)
Pandas(even=6, odd=5)
Pandas(even=90, odd=9)
Pandas(even=10, odd=19)
Pandas(even=44, odd=27)

In [25]: for tup in df.itertuples(index=False, name="Number"):
    ...:     print(tup)
    ...: 
Number(even=2, odd=1)
Number(even=6, odd=5)
Number(even=90, odd=9)
Number(even=10, odd=19)
Number(even=44, odd=27)
```

```python
In [26]: for tup in df.itertuples(index=False, name="Number"):
    ...:     print(tup[0])
    ...: 
2
6
90
10
44

In [27]: for tup in df.itertuples(index=False, name="Number"):
    ...:     print(tup[0], tup.even)
    ...: 
2 2
6 6
90 90
10 10
44 44

In [28]: for tup in df.itertuples(index=False, name="Number"):
    ...:     print(tup[1], tup.odd)
    ...: 
1 1
5 5
9 9
19 19
27 27
```