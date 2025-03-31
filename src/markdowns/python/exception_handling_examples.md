```python
In [1]: try:
   ...:     print("Start...")
   ...:     value = 9 / 4
   ...:     print(f"Operation done..., value = {value}")
   ...: except:
   ...:     print("Error...")
   ...: 
Start...
Operation done..., value = 2.25
```

```python
In [2]: try:
   ...:     print("Start...")
   ...:     value = 9 / 0
   ...:     print(f"Operation done..., value = {value}")
   ...: except:
   ...:     print("Error...")
   ...: 
Start...
Error...
```

```python
In [4]: try:
   ...:     print("Start...")
   ...:     value = 9 / 0
   ...:     print(f"Operation done..., value = {value}")
   ...: except Exception as error:
   ...:     print(f"Error... {error}")
   ...: 
Start...
Error... division by zero
```

