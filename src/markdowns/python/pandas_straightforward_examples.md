```python
In [1]: import pandas as pd

In [2]: pd.__version__
Out[2]: '1.1.5'

In [3]: first_names = pd.Series(["Rishikesh", "Hemkesh", "Malnikesh"])

In [4]: last_names = pd.Series(["Thakur", "Agrawani", "Pujari"])

In [5]: persons_df = pd.DataFrame({"first_name": first_names, "last_name": last_names})

In [6]: persons_df
Out[6]: 
  first_name last_name
0  Rishikesh    Thakur
1    Hemkesh  Agrawani
2  Malnikesh    Pujari

In [7]: persons_df["age"] = [32, 30, 28]

In [8]: persons_df
Out[8]: 
  first_name last_name  age
0  Rishikesh    Thakur   32
1    Hemkesh  Agrawani   30
2  Malnikesh    Pujari   28

In [9]: persons_df.columns
Out[9]: Index(['first_name', 'last_name', 'age'], dtype='object')

In [10]: persons_df.columns.tolist()
Out[10]: ['first_name', 'last_name', 'age']

In [11]: persons_df[["first_name", "age"]]
Out[11]: 
  first_name  age
0  Rishikesh   32
1    Hemkesh   30
2  Malnikesh   28

In [12]: persons_df[["first_name", "age", "last_name"]]
Out[12]: 
  first_name  age last_name
0  Rishikesh   32    Thakur
1    Hemkesh   30  Agrawani
2  Malnikesh   28    Pujari

In [13]: persons_df[["first_name", "last_name", "age"]]
Out[13]: 
  first_name last_name  age
0  Rishikesh    Thakur   32
1    Hemkesh  Agrawani   30
2  Malnikesh    Pujari   28
```

```python
In [14]: persons_df.iloc[[1, 2], [1]]
Out[14]: 
  last_name
1  Agrawani
2    Pujari

In [15]: persons_df.iloc[[1, 2], [0, 1]]
Out[15]: 
  first_name last_name
1    Hemkesh  Agrawani
2  Malnikesh    Pujari

In [16]: persons_df.iloc[[1, 2], [0, 1, 2]]
Out[16]: 
  first_name last_name  age
1    Hemkesh  Agrawani   30
2  Malnikesh    Pujari   28

In [17]: persons_df.iloc[[0, 2], [0, 1, 2]]
Out[17]: 
  first_name last_name  age
0  Rishikesh    Thakur   32
2  Malnikesh    Pujari   28

In [18]: persons_df.iloc[[0, 1], [1, 2]]
Out[18]: 
  last_name  age
0    Thakur   32
1  Agrawani   30

In [19]: persons_df.iloc[[0, 1], 1:]
Out[19]: 
  last_name  age
0    Thakur   32
1  Agrawani   30

In [20]: persons_df.iloc[[0, 1], :2]
Out[20]: 
  first_name last_name
0  Rishikesh    Thakur
1    Hemkesh  Agrawani

In [21]: persons_df.iloc[[0, 1], :3]
Out[21]: 
  first_name last_name  age
0  Rishikesh    Thakur   32
1    Hemkesh  Agrawani   30

In [22]: persons_df.iloc[[0, 1, 2], :3]
Out[22]: 
  first_name last_name  age
0  Rishikesh    Thakur   32
1    Hemkesh  Agrawani   30
2  Malnikesh    Pujari   28

In [23]: persons_df.iloc[:2, :3]
Out[23]: 
  first_name last_name  age
0  Rishikesh    Thakur   32
1    Hemkesh  Agrawani   30

In [24]: persons_df.iloc[:3, :3]
Out[24]: 
  first_name last_name  age
0  Rishikesh    Thakur   32
1    Hemkesh  Agrawani   30
2  Malnikesh    Pujari   28

In [25]: persons_df.iloc[:3, :2] # End index of rows/columns range is exclusive
Out[25]: 
  first_name last_name
0  Rishikesh    Thakur
1    Hemkesh  Agrawani
2  Malnikesh    Pujari

In [26]: persons_df.iloc[0:3, :2] # End index of rows/columns range is exclusive
Out[26]: 
  first_name last_name
0  Rishikesh    Thakur
1    Hemkesh  Agrawani
2  Malnikesh    Pujari

In [27]: persons_df.iloc[0:3, 1:2] # End index of rows/columns range is exclusive
Out[27]: 
  last_name
0    Thakur
1  Agrawani
2    Pujari

In [28]: persons_df.iloc[0:3, 0:2] # Start index of rows/columns range is inclusive
Out[28]: 
  first_name last_name
0  Rishikesh    Thakur
1    Hemkesh  Agrawani
2  Malnikesh    Pujari

In [29]: persons_df.iloc[0:3, 1:2] # Start index of rows/columns  range is inclusive
Out[29]: 
  last_name
0    Thakur
1  Agrawani
2    Pujari
```