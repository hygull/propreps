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

