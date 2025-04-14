```python
In [1]: ooo = "AAA"

In [2]: print(locals())
{'__name__': '__main__', '__doc__': 'Automatically created module for IPython interactive environment', '__package__': None, '__loader__': None, '__spec__': None, '__builtin__': <module 'builtins' (built-in)>, '__builtins__': <module 'builtins' (built-in)>, '_ih': ['', 'ooo = "AAA"', 'print(locals())'], '_oh': {}, '_dh': ['/Users/hygull/Projects/Backend/AiPalette/propreps'], 'In': ['', 'ooo = "AAA"', 'print(locals())'], 'Out': {}, 'get_ipython': <bound method InteractiveShell.get_ipython of <IPython.terminal.interactiveshell.TerminalInteractiveShell object at 0x7fd620b7c048>>, 'exit': <IPython.core.autocall.ExitAutocall object at 0x7fd640355080>, 'quit': <IPython.core.autocall.ExitAutocall object at 0x7fd640355080>, '_': '', '__': '', '___': '', 'pd': <module 'pandas' from '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/__init__.py'>, 'np': <module 'numpy' from '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/numpy/__init__.py'>, '_i': 'ooo = "AAA"', '_ii': '', '_iii': '', '_i1': 'ooo = "AAA"', 'ooo': 'AAA', '_i2': 'print(locals())'}
```

```python
In [4]: locals()["ooo"]
Out[4]: 'AAA'

In [5]: ooo
Out[5]: 'AAA'

In [6]: locals().pop("ooo")
Out[6]: 'AAA'
```

```python
In [7]: ooo
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-2675c65a388a> in <module>
----> 1 ooo

NameError: name 'ooo' is not defined

In [8]: print(ooo)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-65d97388a775> in <module>
----> 1 print(ooo)

NameError: name 'ooo' is not defined
```

```python
In [9]: locals()["ooo"] = "BBB"

In [10]: print(ooo)
BBB
```

```python

In [11]: locals()["-a"] = "BBB"

In [12]: -a
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-12-bd5f19dddee1> in <module>
----> 1 -a

NameError: name 'a' is not defined
```

```python
In [13]: locals()["_a"] = "BBB"

In [14]: _a
Out[14]: 'BBB'
```