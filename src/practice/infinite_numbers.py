import math


# 1st way
n1 = float("inf")
n2 = float("-inf")

print("n1", n1)
print("n2", n2)

# 2nd way
n3 = math.inf
n4 = -math.inf

print("n2", n3)
print("n4", n4)

print("n1 == n3", n1 == n3)
print("n2 == n4", n2 == n4)
print("n1 == n2", n1 == n2)
print("n3 == n4", n3 == n4)
