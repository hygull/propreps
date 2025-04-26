```python
In [1]: import os

In [2]: os.getcwd()
Out[2]: '/Users/hygull/Projects/Backend/AiPalette/propreps'

In [3]: os.listdir()
Out[3]: ['LICENSE', 'README.md', '.git', 'assets', 'src']
```

```bash
In [4]: ls
LICENSE    README.md  assets/    src/

In [5]: ls -al
total 16
drwxr-xr-x   7 hygull  staff   224 Jan 18 22:00 ./
drwxr-xr-x@ 50 hygull  staff  1600 Feb 11 10:02 ../
drwxr-xr-x  15 hygull  staff   480 Feb 21 10:28 .git/
-rw-r--r--   1 hygull  staff  1075 Dec 25 22:21 LICENSE
-rw-r--r--@  1 hygull  staff  1913 Feb 17 22:00 README.md
drwxr-xr-x   3 hygull  staff    96 Dec 29 23:02 assets/
drwxr-xr-x   5 hygull  staff   160 Jan 22 20:50 src/
```

```python
In [6]: cwd = os.getcwd()

In [7]: for dir_content in os.listdir():
   ...:     print(f"{cwd}{os.sep}{dir_content}")
   ...: 
/Users/hygull/Projects/Backend/AiPalette/propreps/LICENSE
/Users/hygull/Projects/Backend/AiPalette/propreps/README.md
/Users/hygull/Projects/Backend/AiPalette/propreps/.git
/Users/hygull/Projects/Backend/AiPalette/propreps/assets
/Users/hygull/Projects/Backend/AiPalette/propreps/src

In [8]: os.path.join("path1", "path2", "path3")
Out[8]: 'path1/path2/path3'

In [10]: for dir_content in os.listdir():
    ...:     print(os.path.join(cwd, dir_content))
    ...: 
/Users/hygull/Projects/Backend/AiPalette/propreps/LICENSE
/Users/hygull/Projects/Backend/AiPalette/propreps/README.md
/Users/hygull/Projects/Backend/AiPalette/propreps/.git
/Users/hygull/Projects/Backend/AiPalette/propreps/assets
/Users/hygull/Projects/Backend/AiPalette/propreps/src
```

```python
In [11]: os.path.abspath(".")
Out[11]: '/Users/hygull/Projects/Backend/AiPalette/propreps'

In [13]: os.path.abspath(".")
Out[13]: '/Users/hygull/Projects/Backend/AiPalette/propreps'

In [16]: os.path.pardir
Out[16]: '..'

In [17]: os.path.abspath(os.path.pardir)
Out[17]: '/Users/hygull/Projects/Backend/AiPalette'

In [18]: os.path.abspath(os.path.curdir)
Out[18]: '/Users/hygull/Projects/Backend/AiPalette/propreps'
```

```python
In [19]: os.path.splitext(os.path.abspath(os.path.curdir))
Out[19]: ('/Users/hygull/Projects/Backend/AiPalette/propreps', '')

In [20]: os.path.splitext("/Users/hygull/Projects/Backend/AiPalette/propreps/README.md")
Out[20]: ('/Users/hygull/Projects/Backend/AiPalette/propreps/README', '.md')
```

```python
In [21]: import os

In [22]: type(os.environ)
Out[22]: os._Environ

In [23]: dir(os.environ)
Out[23]: 
['_MutableMapping__marker',
 '__abstractmethods__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__ior__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__or__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__ror__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__slots__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_abc_impl',
 '_data',
 'clear',
 'copy',
 'decodekey',
 'decodevalue',
 'encodekey',
 'encodevalue',
 'get',
 'items',
 'keys',
 'pop',
 'popitem',
 'setdefault',
 'update',
 'values']

In [24]: isinstance(os.environ, dict)
Out[24]: False
```

