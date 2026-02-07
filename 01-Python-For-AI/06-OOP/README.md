# Object Oriented Programming (OOP) in Python

Object Oriented Programming is a programming paradigm where we organize code using objects and classes instead of only functions.

Instead of writing instructions step-by-step, we model real-world entities inside programs.

---

## What is OOP

OOP focuses on **data + behavior together**.

Example:
A Student has:
- data → name, age, marks
- behavior → study(), take_exam()

Instead of keeping them separate, OOP combines them into one unit called an object.

---

## Procedural vs OOP

### Procedural Programming
Code organized as functions.

```python
name = "Lakshay"
marks = 90

def show_result(name, marks):
    print(name, marks)
```

Data and functions are separate.

---

## Object Oriented Programming

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_result(self):
        print(self.name, self.marks)
```

Data and behavior stay together.

---

## Real World Analogy

Think of a car.

Car:

* properties → color, speed, fuel
* actions → start(), stop(), accelerate()

In OOP:<br>
Car = Class<br>
Specific Car = Object

---

## Benefits of OOP

1. Modularity<br>
Code organized into small units

2. Reusability<br>
Classes reused in multiple programs

3. Maintainability<br>
Easy to update without breaking entire program

4. Real-world Modeling<br>
Complex systems easier to represent

---

## Key Understanding
OOP helps build scalable programs and is heavily used in frameworks, libraries, and machine learning codebases.

---

# Class & Object

A class is a blueprint for creating objects.  
An object is an instance of a class.

---

## Defining a Class

```python
class Student:
    pass
```

`pass` means empty class.

---

## Creating an Object

```python
s1 = Student()
```

`s1` is an object of class Student.

---

## Attributes

Attributes store data inside objects.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## Accessing Attributes

```python
s1 = Student("Lakshay", 23)

print(s1.name)
print(s1.age)
```

---

### Demonstration File

* [class_object_demo.py](class_object_demo.py)

---

# Methods in Class

Methods are functions defined inside a class that describe object behavior.

---

## Instance Methods

An instance method works with object data.

```python
class Student:
    def show(self):
        print("Student method called")
```

---

## self Keyword

`self` refers to the current object.

Python automatically passes the object to methods.

```python
class Student:
    def greet(self):
        print("Hello from", self)
```

---

## Modifying Object State

Methods can update attributes.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks
```

---

### Demonstration File
* [methods_demo.py](methods_demo.py)

---

# Constructors

A constructor is a special method automatically called when an object is created.

In Python the constructor is `__init__`.

---

## __init__ Method

```python
class Student:
    def __init__(self):
        print("Object created")
```

Runs automatically during object creation.

---

## Parameterized Constructor

Takes values while creating object.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

## Default Constructor

Constructor without parameters.

```python
class Student:
    def __init__(self):
        self.name = "Unknown"
```

---

### Demonstration File
* [constructor_demo.py](constructor_demo.py)

---

# Types of Methods

Python supports three types of methods inside a class.

---

## 1. Instance Method

Works with object data.

```python
class Student:
    def show(self):
        print("Instance method")
```

Uses `self` parameter.

---

## 2. Class Method

Works with class-level data.<br>
Uses `cls` and `@classmethod`.

```python
class Student:
    school = "ABC School"

    @classmethod
    def get_school(cls):
        print(cls.school)
```

---

## 3. Static Method

Independent of object and class.<br>
Uses `@staticmethod`.

```python
class Student:
    @staticmethod
    def info():
        print("Static method")
```

---

### Demonstration File
* [method_types_demo.py](method_types_demo.py)

---

# Encapsulation

Encapsulation means restricting direct access to object data and controlling it using methods.

It protects internal data from accidental modification.

---

## Access Levels in Python

### Public

Accessible everywhere.

```python
class Student:
    def __init__(self):
        self.name = "Lakshay"
```

### Protected (Single underscore `_`)

Indicates internal use (convention only).

```python
self._marks = 90
```

### Private (Double underscore `__`)

Not directly accessible outside class.

```python
self.__password = "secret"
```

---

## Getters & Setters

Used to safely access and modify private data.

```python
def get_marks(self):
    return self.__marks

def set_marks(self, value):
    if value >= 0:
        self.__marks = value
```

---

## Data Hiding

Prevents invalid data assignment and improves security.

---

### Demonstration File
* [encapsulation_demo.py](encapsulation_demo.py)

---

# Inheritance

Inheritance allows a class (child) to use properties and methods of another class (parent).

This promotes code reuse.

---

## Single Inheritance

```python
class Person:
    def show(self):
        print("I am a person")

class Student(Person):
    pass
```

Student automatically gets methods of Person.

---

## Accessing Parent Class

```python
s = Student()
s.show()
```

---

## Method Overriding

Child class can modify parent behavior.

```python
class Person:
    def role(self):
        print("General Person")

class Student(Person):
    def role(self):
        print("Student")
```

---

### Demonstration File
* [inheritance_demo.py](inheritance_demo.py)

---

# Multiple & Multilevel Inheritance

Python supports inheriting from multiple classes and inheritance chains.

---

## Multiple Inheritance

A child class inherits from more than one parent class.

```python
class A:
    def show_a(self):
        print("Class A")

class B:
    def show_b(self):
        print("Class B")

class C(A, B):
    pass
```

---

## Multilevel Inheritance

A class inherits from a child class (inheritance chain).

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

### Demonstration Files

* [multiple_inheritance_demo.py](multiple_inheritance_demo.py)
* [multilevel_inheritance_demo.py](multilevel_inheritance_demo.py)

---

# Polymorphism

Polymorphism means "many forms" — the same method name behaves differently depending on the object.

---

## Method Overriding

Child class changes parent method behavior.

```python
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
```

---

## Operator Overloading

Python allows redefining operators for objects using magic methods.

Example: `+` operator

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
```

---

### Demonstration Files

* [polymorphism_demo.py](polymorphism_demo.py)
* [operator_overloading_demo.py](operator_overloading_demo.py)

---

# Abstraction

Abstraction means hiding internal implementation and showing only essential functionality.

In Python, abstraction is implemented using abstract classes from `abc` module.

---

## Abstract Class

A class that cannot be instantiated and acts as a blueprint.

```python
from abc import ABC

class Shape(ABC):
    pass
```

---

## Abstract Methods

Methods declared but not implemented in parent class.<br>
Child classes must implement them.

from abc import ABC, abstractmethod

```python
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

---

### Demonstration File

* [abstraction_demo.py](abstraction_demo.py)

---

# Duck Typing

Duck typing means the type of an object is determined by its behavior, not its class.

"If it walks like a duck and quacks like a duck, it is a duck."

Python does not care about the object’s class — only whether required methods exist.

---

## Concept Example

```python
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def animal_sound(animal):
    animal.speak()
```

Both objects work even though they are unrelated.

---

## Real Python Behavior

```python
animal_sound(Dog())
animal_sound(Cat())
```

No inheritance required — only method presence matters.

---

### Demonstration File
* [duck_typing_demo.py](duck_typing_demo.py)






