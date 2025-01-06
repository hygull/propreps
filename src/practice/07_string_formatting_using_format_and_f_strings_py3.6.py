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
print(f"The Binary format of 8 is {8:b}")

# Octal format
print(f"The Octal format of 8 is {8:o}")

# Hex format, lower case
print(f"The Hex format (lower case) of 31 is {31:x}")

# Hex format, upper case
print(f"The Hex format (upper case) of 31 is {31:X}")
"""
O/P
---
The Binary format of 8 is 1000
The Octal format of 8 is 10
The Hex format (lower case) of 31 is 1f
The Hex format (upper case) of 31 is 1F
"""
