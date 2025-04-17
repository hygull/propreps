```python
In [1]: from datetime import datetime

In [2]: datetime.now()
Out[2]: datetime.datetime(2025, 4, 17, 22, 18, 29, 569792)

In [3]: dir(datetime.now())
Out[3]: 
['__add__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__radd__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rsub__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 'astimezone',
 'combine',
 'ctime',
 'date',
 'day',
 'dst',
 'fold',
 'fromordinal',
 'fromtimestamp',
 'hour',
 'isocalendar',
 'isoformat',
 'isoweekday',
 'max',
 'microsecond',
 'min',
 'minute',
 'month',
 'now',
 'replace',
 'resolution',
 'second',
 'strftime',
 'strptime',
 'time',
 'timestamp',
 'timetuple',
 'timetz',
 'today',
 'toordinal',
 'tzinfo',
 'tzname',
 'utcfromtimestamp',
 'utcnow',
 'utcoffset',
 'utctimetuple',
 'weekday',
 'year']
```

```python
In [4]: now = datetime.now()

In [5]: now.year
Out[5]: 2025

In [6]: now.month
Out[6]: 4

In [7]: now.day
Out[7]: 17

In [8]: now
Out[8]: datetime.datetime(2025, 4, 17, 22, 19, 45, 583385)

In [9]: now.hour
Out[9]: 22

In [10]: now.minute
Out[10]: 19

In [11]: now.second
Out[11]: 45

In [12]: now.microsecond
Out[12]: 583385
```

```python
In [13]: str(now)
Out[13]: '2025-04-17 22:19:45.583385'

In [14]: print(str(now))
2025-04-17 22:19:45.583385
```

```python
In [15]: now.strptime
Out[15]: <function datetime.strptime>

In [16]: now.strftime
Out[16]: <function datetime.strftime>

In [17]: now.strptime("2025-02-28", "%Y-%m-%d")
Out[17]: datetime.datetime(2025, 2, 28, 0, 0)

In [18]: datetime.strptime("2025-02-28", "%Y-%m-%d")
Out[18]: datetime.datetime(2025, 2, 28, 0, 0)

In [19]: now.strftime("%Y-%m-%d")
Out[19]: '2025-04-17'

In [20]: now.strftime("%Y-%m-%d--%H:%M:%S")
Out[20]: '2025-04-17--22:19:45'

In [21]: now.strftime("%Y-%m-%d--%H:%M:%S--%f")
Out[21]: '2025-04-17--22:19:45--583385'
```