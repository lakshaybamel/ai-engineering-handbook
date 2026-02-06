# Looping through lists

numbers = [10, 20, 30, 40]

print("Simple traversal:")
for num in numbers:
    print(num)

print("\nUsing index:")
for i in range(len(numbers)):
    print(i, numbers[i])

print("\nUsing enumerate:")
for index, value in enumerate(numbers):
    print(index, value)

print("\nNested list traversal:")
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for val in row:
        print(val)