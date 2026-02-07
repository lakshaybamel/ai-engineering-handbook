# Flatten a nested list using comprehension

nested = [[1, 2], [3, 4], [5, 6]]

flat = [num for sublist in nested for num in sublist]

print("Flattened list:", flat)
