```python
In [1]: import base64

In [2]: text = b"Python is excellent!"

In [3]: text
Out[3]: b'Python is excellent!'

In [4]: type(text)
Out[4]: bytes

In [5]: encoded = base64.b64encode(text)

In [6]: encoded
Out[6]: b'UHl0aG9uIGlzIGV4Y2VsbGVudCE='

In [7]: encoded.decode("utf-8")
Out[7]: 'UHl0aG9uIGlzIGV4Y2VsbGVudCE='

In [8]: encoded.decode("utf8")
Out[8]: 'UHl0aG9uIGlzIGV4Y2VsbGVudCE='
```
