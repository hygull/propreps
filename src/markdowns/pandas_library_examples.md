### DataFrame's loc (Label based indexing)

```shell
In [1]: import pandas as pd

In [2]: persons_df = pd.DataFrame({
   ...:     "first_name": ["Malinikesh", "Hemkesh", "Rishikesh"],
   ...:     "last_name": ["Agrawani", "Agrawani", "Agarwani"],
   ...:     "age": [28, 30, 32],
   ...: })

In [3]: persons_df
Out[3]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agarwani   32

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
2  Rishikesh  Agarwani   32

In [9]: persons_df.loc[[1, 2], "first_name":"last_name"]
Out[9]: 
  first_name last_name
1    Hemkesh  Agrawani
2  Rishikesh  Agarwani

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
2   Rishikesh  Agarwani

In [12]: persons_df.loc[0:, "first_name":]
Out[12]: 
   first_name last_name  age
0  Malinikesh  Agrawani   28
1     Hemkesh  Agrawani   30
2   Rishikesh  Agarwani   32

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
2   Rishikesh  Agarwani   32

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
2   Rishikesh  Agarwani   32

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
2   Rishikesh  Agarwani

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