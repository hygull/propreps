## Encode

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

## Decode

```python
In [9]: # Decode

In [10]: base64.b64decode(encoded)
Out[10]: b'Python is excellent!'

In [11]: base64.b64decode(encoded).decode("utf-8")
Out[11]: 'Python is excellent!'

In [12]: base64.b64decode(encoded).decode("utf8")
Out[12]: 'Python is excellent!'
```
