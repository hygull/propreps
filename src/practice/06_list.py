numbers = [12, 45, 6, 7, 78, 90, 12.89, 89, 12]
print(numbers)

# Add more numbers
numbers.append(45)
numbers.append(45.90)
numbers.append(14)
print(numbers)

# copy() and count()
numbers2 = numbers.copy()
print(numbers2)
print(numbers2.count(12))

# Print ids
print(id(numbers), id(numbers2))

# Ids of first elements
print(id(numbers[0]), id(numbers2[0]))

# Change the 1st item's value
numbers[0] = 455
print(numbers)
print(numbers2)

# extend()
numbers2.extend([56, 7, 0, 21, 34, 56.0])
numbers2.extend({5000: 12, 6000: 45})
print(numbers2)

numbers3 = numbers2 + numbers
print(numbers3)

# insert()
numbers2.insert(0, 1000)
print(numbers2)
numbers2.pop()
print(numbers2)
numbers2.remove(12)  # Will only remove the first occurrence of the specified element
print(numbers2)

# reverse()
numbers2.reverse()
print(numbers2)

# sort()
numbers2.sort()
print(numbers2)

# index()
print(numbers2.index(12))

# clear()
numbers2.clear()
print(numbers2)


"""
O/P
---
[12, 45, 6, 7, 78, 90, 12.89, 89, 12]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
2
4331866496 4332245888
4357199696 4357199696
[455, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000, 6000]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000, 6000, 455, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
[1000, 12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000, 6000]
[1000, 12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000]
[1000, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14, 56, 7, 0, 21, 34, 56.0, 5000]
[5000, 56.0, 34, 21, 0, 7, 56, 14, 45.9, 45, 12, 89, 12.89, 90, 78, 7, 6, 45, 1000]
[0, 6, 7, 7, 12, 12.89, 14, 21, 34, 45, 45, 45.9, 56.0, 56, 78, 89, 90, 1000, 5000]
4
[]
"""
