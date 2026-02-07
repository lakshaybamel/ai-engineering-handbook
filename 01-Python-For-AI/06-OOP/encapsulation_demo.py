# Encapsulation demonstration

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private variable

    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            print("Invalid marks")

s1 = Student("Lakshay", 85)

print("Marks:", s1.get_marks())

s1.set_marks(95)
print("Updated Marks:", s1.get_marks())

s1.set_marks(-10)   # invalid