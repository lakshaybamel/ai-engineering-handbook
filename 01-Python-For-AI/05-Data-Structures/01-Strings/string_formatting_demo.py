# String formatting demonstration

name = input("Enter your name: ")
age = int(input("Enter your age: "))

# f-string
print(f"Hello {name}, you are {age} years old")

# format()
print("Hello {}, next year you will be {}".format(name, age + 1))

# formatted numbers
pi = 3.14159
print(f"Pi rounded to 2 decimals: {pi:.2f}")

number = 7
print(f"Zero padded number: {number:03}")