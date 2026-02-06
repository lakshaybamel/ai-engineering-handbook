# Functions in Python

A function is a reusable block of code that performs a specific task.

Instead of writing the same logic again and again, we write it once inside a function and reuse it whenever needed.

---

## Why Functions Are Needed

Without functions:
- Code becomes long
- Hard to debug
- Repetition increases errors

With functions:
- Code becomes modular
- Easy to reuse
- Easier debugging
- Cleaner structure

---

## Function Syntax

```python
def greet():
    print("Hello Lakshay Bamel")
```
`def` → keyword used to define a function<br>
`greet` → function name<br>
`()` → parameters<br>
Indented block → function body

---

## Calling a Function

Function runs only when called.

```python
greet()
```
---

## Parameters vs Arguments

### Parameters

Variables written in function definition.

```python
def greet(name):
    print("Hello", name)
```

`name` is parameter


### Arguments

Actual values passed while calling function.

```python
greet("Lakshay")
```

`"Lakshay"` is argument

---

## Return vs Print

### print()

Displays value but does not send it back.

```python
def add(a, b):
    print(a + b)
```

### return

Sends value back to caller.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

Return allows reuse of output.

---

## Local vs Global Scope

### Local Variable

Exists only inside function.

```python
def demo():
    x = 10
    print(x)
```

`x` cannot be accessed outside.

### Global Variable

```python
x = 20

def demo():
    print(x)

demo()
```

Accessible everywhere in program.

---

## Key Understanding

Functions help organize programs into logical blocks.<br>
They reduce repetition and improve readability — which becomes essential in large AI codebases.

---

# Types of Functions

Functions can be categorized based on parameters and return values.

---

## 1. No Parameter No Return

Function neither takes input nor returns output.

```python
def greet():
    print("Hello Lakshay")

greet()
```

Used for fixed operations.

---

## 2. Parameter No Return

Function takes input but does not return anything.

```python
def greet(name):
    print("Hello", name)

greet("Lakshay")
```

Useful when we only need to display or process data.

---

## 3. Parameter With Return

Function takes input and returns a value.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

Most useful type — used heavily in real programs.

---

## 4. Default Arguments

Provides a default value if argument is not given.

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Lakshay")
```

---

## 5. Keyword Arguments

Arguments passed using parameter names.

```python
def student(name, age):
    print(name, age)

student(age=23, name="Lakshay")
```

Order does not matter here.

---

## Key Understanding

Functions allow flexible program design.<br>
Different argument styles help create reusable and configurable logic blocks.

---

### Practice Programs

- [sum_function.py](sum_function.py)
- [max_function.py](max_function.py)
- [even_odd_function.py](even_odd_function.py)
- [factorial_function.py](factorial_function.py)

---

# Recursion

Recursion is when a function calls itself to solve a smaller version of the same problem.

Instead of using loops, the function repeats by calling itself until a stopping condition is reached.

---

## Base Case

Every recursive function must have a stopping condition called the **base case**.

Without a base case → infinite recursion → program crash.

Example idea:
Factorial of 5

5! = 5 × 4 × 3 × 2 × 1

We can define:

n! = n × (n-1)!

Stop when n == 1

---

## Example

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

---

## Stack Behavior (How It Works Internally)

Calling `factorial(4)`:

factorial(4)<br>
→ 4 × factorial(3)<br>
→ 4 × 3 × factorial(2)<br>
→ 4 × 3 × 2 × factorial(1)<br>
→ 4 × 3 × 2 × 1<br>

Then values return back step-by-step.

Each call waits in memory (call stack) until the base case is reached.

---

## Key Understanding

Recursion breaks a big problem into smaller identical problems.<br>
Widely used in trees, graphs, divide-and-conquer algorithms.

---

### Recursive Implementation

- [factorial_recursive.py](factorial_recursive.py)

---

# Lambda Functions

A lambda function is a small anonymous function written in a single line.

Normal functions are defined using `def`  
Lambda functions are defined using `lambda` keyword

---

## Syntax

```python
lambda arguments : expression
```

---

## Example

### Normal function:

```python
def square(x):
    return x * x
```

### Lambda version:

```python
square = lambda x: x * x
print(square(5))
```

---

## Multiple Parameters

```python
add = lambda a, b: a + b
print(add(3, 7))
```
---

## When to Use Lambda

Use lambda when:

* function is small
* used once
* improves readability

Avoid lambda when logic becomes complex — use normal function instead.

---

## Key Understanding

Lambda functions reduce code length and are commonly used with functional tools like map() and filter().

---

### Lambda Demonstration

- [lambda_demo.py](lambda_demo.py)

---

# Functional Programming Tools

Python provides built-in functions to apply operations on collections efficiently.

---

## map()

`map()` applies a function to every element of a sequence.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, numbers))
print(squares)
```

Output:<br>
[1, 4, 9, 16]

---

## filter()

`filter()` selects elements based on a condition.

Syntax:
```python
filter(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
```

Output:<br>
[2, 4, 6]

---

## Key Understanding

map → transforms data<br>
filter → selects data<br>

Both are heavily used in data preprocessing pipelines in Machine Learning.

---

### Functional Tools Demo

- [map_filter_demo.py](map_filter_demo.py)
