### DataFrame's loc (Label based indexing)

```shell
In [1]: import pandas as pd

In [2]: persons_df = pd.DataFrame({
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

In [4]: persons_df.loc[0] # 1st row
Out[4]: 
first_name    Malinikesh
last_name       Agrawani
age                   28
Name: 0, dtype: object

In [5]: persons_df.loc[:, "first_name"] # 1st column
Out[5]: 
0    Malinikesh
1       Hemkesh
2     Rishikesh
Name: first_name, dtype: object

In [6]: persons_df.loc[:, ["first_name", "age"]] # 2 columns
Out[6]: 
   first_name  age
0  Malinikesh   28
1     Hemkesh   30
2   Rishikesh   32

In [7]: persons_df.loc[[1, 2], ["first_name", "age"]] # 2 columns, 2 rows
Out[7]: 
  first_name  age
1    Hemkesh   30
2  Rishikesh   32

In [8]: persons_df.loc[[1, 2], "first_name":"age"]
Out[8]: 
  first_name last_name  age
1    Hemkesh  Agrawani   30
2  Rishikesh  Agrawani   32

In [9]: persons_df.loc[[1, 2], "first_name":"last_name"]
Out[9]: 
  first_name last_name
1    Hemkesh  Agrawani
2  Rishikesh  Agrawani

In [10]: persons_df.loc[0:1, "first_name":"last_name"]
Out[10]: 
   first_name last_name
0  Malinikesh  Agrawani
1     Hemkesh  Agrawani

In [11]: persons_df.loc[0:, "first_name":"last_name"]
Out[11]: 
   first_name last_name
0  Malinikesh  Agrawani
1     Hemkesh  Agrawani
2   Rishikesh  Agrawani

In [12]: persons_df.loc[0:, "first_name":]
Out[12]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agrawani   32

In [13]: 
```


### DataFrame's iloc (Integer-location based indexing)

```shell
In [14]: persons_df.iloc[0]
Out[14]: 
first_name    Malinikesh
last_name       Agrawani
age                   28
Name: 0, dtype: object

In [15]: persons_df.iloc[0:]
Out[15]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agrawani   32

In [16]: persons_df.iloc[0:1]
Out[16]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28

In [17]: persons_df.iloc[0:2]
Out[17]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30

In [18]: persons_df.iloc[0:3]
Out[18]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agrawani   32

In [19]: persons_df.iloc[0:3, 0:1]
Out[19]: 
   first_name
0  Malinikesh
1     Hemkesh
2   Rishikesh

In [20]: persons_df.iloc[0:3, 0:2]
Out[20]: 
   first_name last_name
0  Malinikesh  Agrawani
1     Hemkesh  Agrawani
2   Rishikesh  Agrawani

In [21]: persons_df.iloc[0:3, "first_name"]
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

# Filtering

```shell
In [21]: persons_df
Out[21]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agrawani   32

In [22]: persons_df.loc[persons_df["age"] > 30]
Out[22]: 
  first_name last_name  age
2  Rishikesh  Agrawani   32

In [23]: persons_df.loc[persons_df["age"] == 30]
Out[23]: 
  first_name last_name  age
1    Hemkesh  Agrawani   30

In [24]: persons_df.loc[persons_df["age"] < 30]
Out[24]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28

In [25]: persons_df.loc[persons_df["age"] <= 30]
Out[25]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
```

```shell
In [27]: persons_df.loc[(persons_df["age"] <= 30) & (persons_df["first_name"].isin(["Malinikesh  Agrawani", "Hemkesh  Agrawani"]))]
Out[27]: 
Empty DataFrame
Columns: [first_name, last_name, age]
Index: []

In [28]: persons_df.loc[(persons_df["age"] <= 30) & (persons_df["first_name"].isin(["Malinikesh", "Hemkesh"]))]
Out[28]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
```


```shell
In [29]: persons_df.loc[persons_df["age"] <= 30]
Out[29]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30

In [30]: persons_df.loc[persons_df["age"] == 30, "first_name"] = "Hem"

In [31]: persons_df
Out[31]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1         Hem  Agrawani   30
2   Rishikesh  Agrawani   32

In [32]: persons_df.loc[persons_df["age"] == 32, "first_name"] = "Rishi"

In [33]: persons_df.loc[persons_df["age"] == 28, "first_name"] = "Malini"

In [34]: persons_df
Out[34]: 
  first_name last_name  age
0     Malini  Agrawani   28
1        Hem  Agrawani   30
2      Rishi  Agrawani   32
```

```shell
In [35]: persons_df.index
Out[35]: RangeIndex(start=0, stop=3, step=1)

In [36]: persons_df.index.tolist()
Out[36]: [0, 1, 2]

In [37]: persons_df.columns.tolist()
Out[37]: ['first_name', 'last_name', 'age']

In [38]: persons_df.columns
Out[38]: Index(['first_name', 'last_name', 'age'], dtype='object')
```

