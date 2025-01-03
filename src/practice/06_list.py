numbers = [12, 45, 6, 7, 78, 90, 12.89, 89, 12]
print("+ ->", numbers)

# Add more numbers
numbers.append(45)
numbers.append(45.90)
numbers.append(14)
print("A ->", numbers)

# copy() and count()
numbers2 = numbers.copy()
print("B ->", numbers2)
print("C ->", numbers2.count(12))

# Print ids
print("D ->", id(numbers), id(numbers2))

# Ids of first elements
print("E ->", id(numbers[0]), id(numbers2[0]))

# Change the 1st item's value
numbers[0] = 455
print("F ->", numbers)
print("G ->", numbers2)

# extend()
numbers2.extend([56, 7, 0, 21, 34, 56.0])
numbers2.extend({5000: 12, 6000: 45})
print("H ->", numbers2)

numbers3 = numbers2 + numbers
print("I ->", numbers3)

# insert()
numbers2.insert(0, 1000)
print("J ->", numbers2)
numbers2.pop()
print("K ->", numbers2)
numbers2.remove(12)  # Will only remove the first occurrence of the specified element
print("L ->", numbers2)

# reverse()
numbers2.reverse()
print("M ->", numbers2)

# sort()
numbers2.sort()
print("N ->", numbers2)

# index()
print("O ->", numbers2.index(12))

# clear()
numbers2.clear()
print("P ->", numbers2)


"""
O/P
---
+ -> [12, 45, 6, 7, 78, 90, 12.89, 89, 12]
A -> [12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
B -> [12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
C -> 2
D -> 4369664384 4369666304
E -> 4394997584 4394997584
F -> [455, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
G -> [12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
H -> [12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000, 6000]
I -> [12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000, 6000, 455, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
J -> [1000, 12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000, 6000]
K -> [1000, 12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000]
L -> [1000, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000]
M -> [5000, 56.0, 34, 21, 0, 7, 56, 14, 45.9, 45, 12, 89, 12.89, 90, 78, 7, 6, 45, 1000]
N -> [0, 6, 7, 7, 12, 12.89, 14, 21, 34, 45, 45, 45.9, 56.0, 56, 78, 89, 90, 1000, 5000]
O -> 4
P -> []
"""
