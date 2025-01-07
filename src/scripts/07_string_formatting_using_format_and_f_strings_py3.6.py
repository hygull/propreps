"""
Command:
    - python3 src/scripts/07_string_formatting_using_format_and_f_strings_py3.6.py
"""

fullname = "Rishikesh Agrawani"
age = 32
pi = 3.142

print(
    f"My name is {fullname} and I am {age} years old. I like math constant PI i.e. {pi:.2f}."
)
"""
O/P
---
My name is Rishikesh Agrawani and I am 32 years old. I like math constant PI i.e. 3.14.
"""

# Placeholder -> {}, Modifier -> , (Use a comma as a thousand separator)
print(f"Dwaparyuga is {5000:,} years old.")

# Left aligns the result (within the available space)
print(f"Sometimes we more think about {100:<10} different ways to solve a problem.")

# Right aligns the result (within the available space)
print(f"Sometimes we more think about {100:>10} different ways to solve a problem.")

# Center aligns the result (within the available space)
print(f"Sometimes we more think about {100:^10} different ways to solve a problem.")

# Use a plus sign to indicate if the result is positive or negative
print(f"I like positive numbers like {45 + 5:+} and negative numbers like {-10 + 5:+}.")
"""
O/P
---
Dwaparyuga is 5,000 years old.
Sometimes we more think about 100        different ways to solve a problem.
Sometimes we more think about        100 different ways to solve a problem.
Sometimes we more think about    100     different ways to solve a problem.
I like positive numbers like +50 and negative numbers like -5.
"""

# Binary format
print(f"The Binary format of 8 is {8:b}.")

# Octal format
print(f"The Octal format of 8 is {8:o}.")

# Hex format, lower case
print(f"The Hex format (lower case) of 31 is {31:x}.")

# Hex format, upper case
print(f"The Hex format (upper case) of 31 is {31:X}.")
"""
O/P
---
The Binary format of 8 is 1000.
The Octal format of 8 is 10.
The Hex format (lower case) of 31 is 1f.
The Hex format (upper case) of 31 is 1F.
"""


# Operations on f-strings i.e. math operation in the placeholders
print(f"My favourite number is {1700 + 29}.")

# Performing math operations on variables
four = 3
two = 2
print(f"There are total {two + 3 + 1} days in a week.")

# if...else inside placeholders
num = 4
print(f"{num} is an {'even' if num % 2 == 0 else 'odd'} number.")


# Execute functions inside the placeholders
def hello():
    return "Hello programmers!"


print(f"Once I woke up very early in the morning and saw a message -> {hello()}")

"""
O/P
---
My favourite number is 1729.
There are total 6 days in a week.
4 is an even number.
Once I woke up very early in the morning and saw a message -> Hello programmers!
"""


# String formatting using format()
print("My name is {} and I am {} years old.".format("Rishikesh Agrawani", 32))

# If we do not use index numbers then -> My name is 32 and I am Rishikesh Agrawani years old.
print("My name is {1} and I am {0} years old.".format(32, "Rishikesh Agrawani"))

# Named indexes
print(
    "My name is {fullname} and I am {age} years old.".format(
        age=30, fullname="Hemkesh Agrawani"
    )
)
print(
    "My name is {fullname} and I am {age} years old.".format(
        fullname="Malinikesh Agrawani", age=28
    )
)

"""
O/P
---
My name is Rishikesh Agrawani and I am 32 years old.
My name is Rishikesh Agrawani and I am 32 years old.
My name is Hemkesh Agrawani and I am 30 years old.
My name is Malinikesh Agrawani and I am 28 years old.
"""
