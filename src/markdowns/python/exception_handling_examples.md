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

```python
In [5]: try:
   ...:     print("Start...")
   ...:     value = 9 / 0
   ...:     print(f"Operation done..., value = {value}")
   ...: except Exception as error:
   ...:     print(f"Error -> {error}")
   ...: except ZeroDivisionError as error:
   ...:     print(f"Error => {error}")
   ...: 
Start...
Error -> division by zero
```

```python
In [6]: try:
   ...:     print("Start...")
   ...:     value = 9 / 0
   ...:     print(f"Operation done..., value = {value}")
   ...: except ZeroDivisionError as error:
   ...:     print(f"Error -> {error}")
   ...: except Exception as error:
   ...:     print(f"Error => {error}")
   ...: 
Start...
Error -> division by zero
```

```python
In [7]: try:
   ...:     print("Start...")
   ...:     value = 9 / 0
   ...:     print(f"Operation done..., value = {value}")
   ...: except ZeroDivisionError as error:
   ...:     print(f"Error => {error}")
   ...: except Exception as error:
   ...:     print(f"Error -> {error}")
   ...: 
Start...
Error => division by zero
```

```python
In [8]: try:
   ...:     print("Start...")
   ...:     value = 9 / 0
   ...:     print(f"Operation done..., value = {value}")
   ...: except ValueError as error:
   ...:     print(f"Error --> {error}")
   ...: except ZeroDivisionError as error:
   ...:     print(f"Error => {error}")
   ...: except Exception as error:
   ...:     print(f"Error -> {error}")
   ...: 
Start...
Error => division by zero
```

```python
In [9]: try:
   ...:     print("Start...")
   ...:     value = int("Rishi")
   ...:     print(f"Operation done..., value = {value}")
   ...: except ValueError as error:
   ...:     print(f"Error --> {error}")
   ...: except ZeroDivisionError as error:
   ...:     print(f"Error => {error}")
   ...: except Exception as error:
   ...:     print(f"Error -> {error}")
   ...: 
Start...
Error --> invalid literal for int() with base 10: 'Rishi'
```

```python
In [10]: try:
    ...:     print("Start...")
    ...:     value = int("Rishi")
    ...:     print(f"Operation done..., value = {value}")
    ...: #except ValueError as error:
    ...: #    print(f"Error --> {error}")
    ...: except ZeroDivisionError as error:
    ...:     print(f"Error => {error}")
    ...: except Exception as error:
    ...:     print(f"Error -> {error}")
    ...: 
Start...
Error -> invalid literal for int() with base 10: 'Rishi'
```