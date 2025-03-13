```python
In [1]: def adder(num1, num2):
   ...:     return num1 + num2
   ...: 

In [2]: adder(12, 8)
Out[2]: 20

In [3]: adder(12, 88)
Out[3]: 100
```

```python
In [4]: # Lambda function

In [5]: get_sum = lambda num1, num2: num1 + num2

In [6]: get_sum(1, 3)
Out[6]: 4

In [7]: get_sum(100, 300)
Out[7]: 400
```

```python
In [15]: print_numbers = lambda even, odd, temp: print(f"odd -> {odd}, even ->{even}, temp -> {temp}")

In [16]: print_numbers(12, 45, 67.0)
odd -> 45, even ->12, temp -> 67.0
```

```python
In [21]: def get_greeter(greet_beginner):
    ...:     return lambda fullname: f"%s {fullname}! How are you doing?" % (greet_beginner)
    ...: 

In [22]: greeter = get_greeter("Hi")

In [23]: greeter("Rishikesh")
Out[23]: 'Hi Rishikesh! How are you doing?'
```