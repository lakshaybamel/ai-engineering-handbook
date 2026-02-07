# Constructor demonstration

class Student:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

# parameterized
s1 = Student("Lakshay", 23)

# default
s2 = Student()

s1.show()
s2.show()

