# Mathematical set operations

a = set(map(int, input("Enter elements of set A: ").split()))
b = set(map(int, input("Enter elements of set B: ").split()))

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (A-B):", a - b)
print("Symmetric Difference:", a ^ b)