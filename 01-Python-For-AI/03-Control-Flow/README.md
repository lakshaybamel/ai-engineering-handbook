# Control Flow in Python

Control Flow decides how a program makes decisions instead of executing every line sequentially.

In real programs we don't always run all instructions —
we choose paths based on conditions.

---

## Why Control Flow Matters

Machine Learning models later depend heavily on logic:
- filtering data
- checking conditions
- stopping training
- validating input

So learning control flow is learning **how programs think**.

---

# 1. Conditional Statements

Conditional statements allow a program to execute code only when a condition is true.

---

## if Statement

The simplest decision making statement.

```python
age = 20

if age >= 18:
    print("Lakshay is eligible to vote")
```
If condition is True → block runs<br>
If False → skipped

---

## if-else Statement

Used when program must choose between two paths.

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## if-elif-else Statement

Used when there are multiple conditions.

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```
The program stops checking once a condition becomes true.

---

## Nested Conditions

A condition inside another condition.

```python
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
```

---

## match-case (Switch Alternative)

Cleaner way to compare one value against many options.

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")
```
Useful when checking many exact values instead of ranges.

---

## Importance of Indentation

Python does not use braces `{ }`
Indentation defines code blocks.

#### Correct:
```python
if True:
    print("Runs")
```

#### Wrong:
```python
if True:
print("Error")
```

This causes an IndentationError

---
## Practice Programs

Implementation files for these concepts:

* [odd_even.py](./odd_even.py)
* [largest_of_three.py](./largest_of_three.py)
* [vote_check.py](./vote_check.py)
* [grade_calculator.py](./grade_calculator.py)

---

# 2. Loops

Loops allow a program to repeat instructions multiple times automatically.

Instead of writing the same code again and again, we use loops to automate repetition.

---

## while Loop

Runs as long as the condition remains True.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```
**Flow:**<br>
1 → check condition<br>
2 → execute block<br>
3 → update variable<br>
4 → repeat<br>

If condition never becomes False → infinite loop

---

## for Loop

Used when the number of iterations is known.

```python
for i in range(1, 6):
    print(i)
```

More readable and safer than while loop in most cases.

---

## range() Function

Generates a sequence of numbers.

#### Forms:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

#### Examples:

```python
range(5)        # 0 1 2 3 4
range(1, 5)     # 1 2 3 4
range(1, 10, 2) # 1 3 5 7 9
```

---

## Loop Flow Understanding

Every loop follows a pattern:

**Initialization → Condition → Execution → Update → Repeat**

#### Example:

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

---

## Nested Loops

A loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Outer loop controls rows<br>
Inner loop controls columns

Used in patterns, matrices, grids.

---

## Practice Programs

Implementation files for loops:

* [multiplication_table.py](./multiplication_table.py)
* [sum_of_n.py](./sum_of_n.py)
* [factorial_loop.py](./factorial_loop.py)
* [vowel_counter.py](./vowel_counter.py)

---

# 3. Loop Control Statements

Loop control statements change the normal execution flow of a loop.

---

## break

Immediately stops the loop.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```
Output:<br>
1 2 3 4

---

## continue

Skips the current iteration and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:<br>
1 2 4 5

---

## pass

Does nothing.
Used as a placeholder when a statement is required syntactically.

```python
for i in range(3):
    pass
```

Useful when writing incomplete code structures.

---

## Demonstration File

See implementation:

* [loop_control_demo.py](/loop_control_demo.py)