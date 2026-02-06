# map and filter demonstration

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# square each number
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)