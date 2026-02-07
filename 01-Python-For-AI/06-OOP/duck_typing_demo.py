# Duck typing demonstration

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

class Bird:
    def speak(self):
        print("Bird chirps")

def animal_sound(animal):
    animal.speak()

animals = [Dog(), Cat(), Bird()]

for a in animals:
    animal_sound(a)