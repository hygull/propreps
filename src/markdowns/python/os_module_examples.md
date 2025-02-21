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