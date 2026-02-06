# Simple student record system

student = {}

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))
student["course"] = input("Enter course: ")

print("\nStudent Record:")
for key, value in student.items():
    print(key, ":", value)
