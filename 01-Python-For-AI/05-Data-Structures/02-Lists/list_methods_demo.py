# Demonstration of list methods

nums = [3, 1, 4, 1, 5]

print("Original:", nums)

nums.append(9)
print("After append:", nums)

nums.insert(1, 7)
print("After insert:", nums)

nums.extend([2, 6])
print("After extend:", nums)

nums.remove(1)
print("After remove:", nums)

nums.pop()
print("After pop:", nums)

nums.sort()
print("Sorted:", nums)

nums.reverse()
print("Reversed:", nums)

print("Count of 1:", nums.count(1))
print("Index of 4:", nums.index(4))