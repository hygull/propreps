```python
In [3]: locals()["full_name"] = "Rishikesh Agrawani"

In [4]: full_name
Out[4]: 'Rishikesh Agrawani'

In [5]: locals()["age"] = 32

In [6]: age
Out[6]: 32

In [7]: locals().pop("age")
Out[7]: 32

In [8]: age
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[8], line 1
----> 1 age

NameError: name 'age' is not defined

```

```python
In [9]:  locals().pop("full_name")
Out[9]: 'Rishikesh Agrawani'

In [10]: full_name
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[10], line 1
----> 1 full_name

NameError: name 'full_name' is not defined
```