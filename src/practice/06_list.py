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

"""
O/P
---
[12, 45, 6, 7, 78, 90, 12.89, 89, 12]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
2
4308978048 4309357440
ip-192-168-29-16:propreps hygull$ python3 src/practice/06_list.py 
[12, 45, 6, 7, 78, 90, 12.89, 89, 12]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
2
4365912448 4366291840
4391245648 4391245648
ip-192-168-29-16:propreps hygull$ python3 src/practice/06_list.py 
[12, 45, 6, 7, 78, 90, 12.89, 89, 12]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
2
4304374144 4304753536
4329707344 4329707344
[455, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
[12, 45, 6, 7, 78, 90, 12.89, 89, 12, 45, 45.9, 14]
"""
