# Common elements between two lists

a = set(map(int, input("Enter list A: ").split()))
b = set(map(int, input("Enter list B: ").split()))

print("Common elements:", a & b)
