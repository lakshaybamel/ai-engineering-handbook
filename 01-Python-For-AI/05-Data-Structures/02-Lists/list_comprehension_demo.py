# List comprehension demonstration

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# square numbers
squares = [x*x for x in numbers]
print("Squares:", squares)

# even numbers
evens = [x for x in numbers if x % 2 == 0]
print("Evens:", evens)

# label odd/even
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Labels:", labels)