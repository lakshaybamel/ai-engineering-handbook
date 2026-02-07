# Exception Handling in Python

An exception is an error that occurs during program execution (runtime).

When an exception happens, the program stops unless handled properly.

---

## What is an Exception

Example:

```python
print(10 / 0)
```

This causes:

ZeroDivisionError

The program crashes immediately.

---

## Runtime Errors vs Syntax Errors

### Syntax Error

Mistake in code structure.

```python
if True
    print("Hello")
```

Detected before program runs.


### Runtime Error (Exception)

Occurs during execution.

```python
num = int("abc")
```

Program starts but crashes while running.

---

## Why Exception Handling is Needed

#### Without handling:

* program crashes
* user loses data
* bad user experience

#### With handling:

* program continues
* user-friendly messages
* safer applications

---

## Key Understanding

Real-world programs must handle errors because users and data are unpredictable.

---


# try & except

`try` block contains risky code.  
`except` block runs if an error occurs.

```python
try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Something went wrong")
```

Program does not crash.

--

## Specific Exception Types

We should catch exact errors instead of generic except.

```python
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
```

---

### Demonstration File
* [try_except_demo.py](try_except_demo.py)

---

# Multiple Exceptions

A program may generate different types of errors.  
We can handle each error separately for better user feedback.

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)

except ZeroDivisionError:
    print("Division by zero not allowed")

except ValueError:
    print("Please enter numeric values")
```

Each error is handled independently.

---

### Demonstration File

* [multiple_except_demo.py](multiple_except_demo.py)

---

# else & finally

Python provides extra blocks with try-except for better control.

---

## else Block

Runs only if no exception occurs.

```python
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
```

---

## finally Block

Runs always, whether error occurs or not.

Used for cleanup operations like closing files or releasing resources.

```python
try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Error occurred")
finally:
    print("Execution finished")
```

---

## Guaranteed Execution

finally ensures important code always runs.

---

### Demonstration File

* [finally_demo.py](finally_demo.py)

---

# Raising Exceptions

Python allows manually generating errors using `raise`.

Used when program detects invalid conditions.

---

## raise Keyword

```python
age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## Custom Error Messages

We can attach meaningful messages.

```python
marks = int(input("Enter marks: "))

if marks > 100:
    raise Exception("Marks cannot exceed 100")
```

---

### Demonstration File

* [raise_exception_demo.py](raise_exception_demo.py)

---

# Custom Exceptions

Python allows creating user-defined exception classes for specific situations.

Helps make programs more readable and meaningful.

---

## Creating Custom Exception

```python
class NegativeAgeError(Exception):
    pass
```

---

## Using Custom Exception

```python
age = int(input("Enter age: "))

if age < 0:
    raise NegativeAgeError("Age cannot be negative")
```

---

### Demonstration File

* [custom_exception_demo.py](custom_exception_demo.py)

---

# Practice Programs

* [safe_division.py](safe_division.py)
* [input_validation.py](input_validation.py)




