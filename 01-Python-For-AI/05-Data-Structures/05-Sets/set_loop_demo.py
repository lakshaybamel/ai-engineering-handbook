# Iterating and membership test

s = set(map(int, input("Enter elements: ").split()))

print("Elements:")
for value in s:
    print(value)

num = int(input("Enter number to search: "))
print("Exists:", num in s)