# Raising exceptions demonstration

try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Age accepted:", age)

except ValueError as e:
    print("Error:", e)