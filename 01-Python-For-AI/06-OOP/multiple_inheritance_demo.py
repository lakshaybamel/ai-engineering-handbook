# Multiple inheritance demonstration

class Father:
    def skills(self):
        print("Driving")

class Mother:
    def hobby(self):
        print("Painting")

class Child(Father, Mother):
    def show(self):
        print("Child inherits both")

c = Child()
c.skills()
c.hobby()
c.show()