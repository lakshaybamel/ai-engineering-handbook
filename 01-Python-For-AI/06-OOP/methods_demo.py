# Methods demonstration

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, "has marks", self.marks)

    def update_marks(self, new_marks):
        self.marks = new_marks

s1 = Student("Lakshay", 80)

s1.show()
s1.update_marks(95)
s1.show()