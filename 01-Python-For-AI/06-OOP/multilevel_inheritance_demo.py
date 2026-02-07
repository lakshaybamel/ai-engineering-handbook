# Multilevel inheritance demonstration

class Person:
    def identity(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("I study")

class Graduate(Student):
    def degree(self):
        print("I have a degree")

g = Graduate()
g.identity()
g.study()
g.degree()