# Looping through dictionary

student = {"name": "Lakshay", "age": 23, "city": "Delhi"}

print("Keys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)