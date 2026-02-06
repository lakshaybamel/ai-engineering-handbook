# Lambda function demonstration

square = lambda x: x * x
add = lambda a, b: a + b

num = int(input("Enter a number: "))
print("Square:", square(num))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", add(x, y))