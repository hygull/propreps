```python
In [1]: def gen_numbers(total_numbers=0, numbers_type=None):
   ...:     if numbers_type is None:
   ...:         return []
   ...: 
   ...:     if numbers_type == "even":
   ...:         start_num = 0
   ...:     elif numbers_type == "odd":
   ...:         start_num = 1
   ...: 
   ...:     for num in range(total_numbers):
   ...:         yield start_num
   ...:         start_num += 2
   ...: 

In [2]: for number in gen_numbers(total_numbers=10, numbers_type="odd"):
   ...:     print(number)
   ...: 
1
3
5
7
9
11
13
15
17
19

In [3]: for number in gen_numbers(total_numbers=10, numbers_type="even"):
   ...:     print(number)
   ...: 
0
2
4
6
8
10
12
14
16
18

In [4]: 
```