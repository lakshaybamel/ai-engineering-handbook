# Function to find maximum of two numbers

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Maximum =", find_max(x, y))
