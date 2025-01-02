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


# *-------- Another example ---------*
def print_lords_incarnations_details(lord_name1, lord_name2):
    match (lord_name1, lord_name2):
        case ("Ram", "Krishna") | ("Parshuram", "Narsingh"):
            print(
                f"Lord {lord_name1} ji and lord {lord_name2} ji, both are incarnations of Lord shri Hari Narayana Vishnu ji."
            )
        case ("Kal Bhairav", "Hanuman"):
            print(
                f"Lord {lord_name1} ji and lord {lord_name2} ji, both are incarnations of Lord Mahadev ji."
            )


print_lords_incarnations_details("Parshuram", "Narsingh")
print_lords_incarnations_details("Kal Bhairav", "Hanuman")
print_lords_incarnations_details("Ram", "Krishna")
print_lords_incarnations_details("Buddha", "Krishna")  # Won't be printed
"""
O/P
---
Lord Parshuram ji and lord Narsingh ji, both are incarnations of Lord shri Hari Narayana Vishnu ji.
Lord Kal Bhairav ji and lord Hanuman ji, both are incarnations of Lord Mahadev ji.
Lord Ram ji and lord Krishna ji, both are incarnations of Lord shri Hari Narayana Vishnu ji.
"""
