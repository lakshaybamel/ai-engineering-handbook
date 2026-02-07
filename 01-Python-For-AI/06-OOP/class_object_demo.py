# Class and Object demonstration

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# creating object
s1 = Student("Lakshay", 23)

# accessing attributes
print("Name:", s1.name)
print("Age:", s1.age)