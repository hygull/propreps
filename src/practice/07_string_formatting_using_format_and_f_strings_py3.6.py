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
"""
O/P
---
Dwaparyuga is 5,000 years old.
Sometimes we more think about 100        different ways to solve a problem.
Sometimes we more think about        100 different ways to solve a problem.
Sometimes we more think about    100     different ways to solve a problem.
"""
