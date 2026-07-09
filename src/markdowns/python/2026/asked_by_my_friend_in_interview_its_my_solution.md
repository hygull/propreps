```python
In [1]: import re

In [2]: string = "A12B5"

In [3]: "".join(ch * int(str_num) for ch, str_num in zip([c for c in re.split("\d+", string) if c], [d for d in re.split("[a-zA-Z]+", string) if d]))
Out[3]: 'AAAAAAAAAAAABBBBB'
```


```python
In [4]: "".join(ch * int(str_num) for ch, str_num in zip(re.findall("\D+", string), re.findall("\d+", string)))
Out[4]: 'AAAAAAAAAAAABBBBB'
```
