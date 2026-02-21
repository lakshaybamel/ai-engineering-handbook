# Calculus for AI/ML

Calculus is used to understand how things change.

In Machine Learning:
- models learn by adjusting parameters
- calculus helps us optimize those parameters

---

## Why Calculus is Important

Used in:
- gradient descent
- loss minimization
- neural networks

---

# Functions

A function maps input → output

```
f(x) = x^2
```

---

## Composite Functions

Function inside another function:

```
f(g(x))
```

---

## Scalar Operations on Functions

```
2f(x)
f(x) + g(x)
```

---

## Input Transformations

```
f(2x)
f(x + 1)
```

---

# Differentiation

Derivative = rate of change

```
f'(x)
```

---

## Basic Differentiation Rules

### Power Rule

```
d/dx (x^n) = n * x^(n-1)
```

### Constant Rule

```
d/dx (c) = 0
```

### Sum Rule

```
d/dx (f + g) = f' + g'
```

### Product Rule

```
d/dx (f*g) = f'g + fg'
```

### Chain Rule (Very Important)

```
d/dx f(g(x)) = f'(g(x)) * g'(x)
```

---

## Minima & Maxima

Critical points occur when:

```
f'(x) = 0
```

Used to find:

- minimum (best solution)
- maximum

---

## ML Insight

- training = minimizing loss function
- derivative tells direction to move

---

## Gradient Descent (Concept)

Idea:
1. start with random value
2. compute derivative
3. update value
4. repeat

Goal → reach minimum loss

---

## Key Takeaways

- derivative → slope
- chain rule → core of deep learning
- minima → optimal solution

---

## Mental Model

Calculus answers:

👉 "How to optimize and improve a model?"