# Custom exception demonstration

class NegativeAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))

    if age < 0:
        raise NegativeAgeError("Age cannot be negative")

    print("Valid age:", age)

except NegativeAgeError as e:
    print("Custom Error:", e)

except ValueError:
    print("Invalid numeric input")