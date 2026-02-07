# Types of methods demonstration

class Student:
    school = "BIT Mesra"

    # instance method
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student:", self.name)

    # class method
    @classmethod
    def school_name(cls):
        print("School:", cls.school)

    # static method
    @staticmethod
    def greet():
        print("Welcome to OOP")

s1 = Student("Lakshay")

s1.show()
Student.school_name()
Student.greet()