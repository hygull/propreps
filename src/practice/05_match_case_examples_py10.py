"""
Command
=======
	python src/practice/05_match_case_examples_py10.py
"""


# Normal example
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
