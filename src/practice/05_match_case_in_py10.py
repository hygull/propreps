"""
Command to run the script
=========================
	python src/practice/05_match_case_in_py10.py

Note
====
	- Patterns must be literal values, variables, or other valid pattern elements.
	- Expressions like 45 - 35 and 60 + 7 are evaluated at runtime, which is not compatible with pattern matching's static evaluation.
"""


# *------- Normal example -------*
fullname = "Hemkesh Agrawani"


match fullname:
    case "Rishikesh Agrawani":
        print(f"{fullname} is an elder brother")
    case "Hemkesh Agrawani" | "Malinikesh Agrawani":
        print(f"{fullname} is a sibling of Rishikesh Agrawani")
    case _:
        print(f"{fullname} does not seem to be from Rishikesh Agrawani's siblings list")
"""
O/P
---
Hemkesh Agrawani is sibling of Rishikesh Agrawani
"""

# *------- AND condition without using Guards (if conditions) -------*
num1, num2 = 10, 67

value1 = 45 - 35
value2 = 60 + 7
value3 = 35 - 25
value4 = 50 + 17

match (num1, num2):
    case (value1, value2):
        print("I prefer coding very often when I get time")
    case (value3, value4):
        print("I love coding")
    case _:
        print("Coding should be a hobby as well and not just a source to earn money")
"""
O/P
---
I prefer coding very often when I get time
"""


# *------- AND condition using Guards (if conditions)  -------*
match (num1, num2):
    case (value1, value2) if value1 > value2:
        print("I prefer coding very often when I get time")
    case (value3, value4) if value1 < value2:
        print("I love coding")
    case _:
        print("Coding should be a hobby as well and not just a source to earn money")
"""
O/P
---
I love coding
"""
