# Advanced comprehension demonstration

matrix = [[1, 2, 3], [4, 5, 6]]

flatten = [num for row in matrix for num in row]
print("Flatten:", flatten)

numbers = [1, 2, 3, 4, 5]

squares = {x: x*x for x in numbers}
print("Squares:", squares)

even_squares = {x: x*x for x in numbers if x % 2 == 0}
print("Even squares:", even_squares)