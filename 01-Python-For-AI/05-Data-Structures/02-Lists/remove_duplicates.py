# Remove duplicates from a list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)
