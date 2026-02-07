# Inheritance demonstration

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

    def role(self):
        print("Role: Person")

class Student(Person):
    def role(self):
        print("Role: Student")

s1 = Student("Lakshay")

s1.show()
s1.role()