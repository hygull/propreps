import pandas as pd


df = pd.DataFrame(
    {"first_name": ["Rishikesh", "Hemkesh", "Malinikesh"], "age": [32, 30, 28]}
)
df["last_name"] = "Agrawani"

print(df)
"""
OUTPUT (python3 src/practice/03_dataframes.py)
==============================================

   first_name  age last_name
0   Rishikesh   32  Agrawani
1     Hemkesh   30  Agrawani
2  Malinikesh   28  Agrawani
"""
