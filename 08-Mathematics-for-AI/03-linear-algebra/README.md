# Linear Algebra for AI/ML

Linear Algebra is the backbone of Machine Learning.

It helps us represent:
- data → vectors
- datasets → matrices
- transformations → matrix operations

---

## Why Linear Algebra is Important

Used in:
- data representation
- neural networks
- feature transformations
- computer vision

---

## Straight Lines

Equation of a line:

```
y = mx + c
```

- m → slope
- c → intercept

---

## Distance Between Two Points

```
distance = √((x2 - x1)^2 + (y2 - y1)^2)
```

---

## Parallel & Perpendicular Lines

- Parallel → same slope
- Perpendicular → product of slopes = -1

---

## Vectors

A vector represents magnitude and direction.

Example:

```
v = [2, 3]
```

### Vector Addition

```
[1,2] + [3,4] = [4,6]
```

### Scalar Multiplication

```
2 * [1,2] = [2,4]
```

### Dot Product (Very Important)

```
a · b = a1*b1 + a2*b2
```

Used for:

- similarity (cosine similarity)
- projections

### Cross Product

Used in 3D space.

### ML Insight

- dot product → similarity between vectors
- used in recommendation systems & embeddings
 
---

## Matrices

Matrix = 2D array

```
A = [[1,2],
     [3,4]]
```

---

## Matrix Operations

### Addition

```
A + B
```

### Multiplication

```
A × B
```

Important:
- columns of A = rows of B

---

## Determinant

```
|A|
```

Used to check:

- matrix invertibility

---

## Eigenvalues & Eigenvectors

Very important for ML.

They represent:
- direction of data
- importance of features

---

## ML Insight

Used in:

- PCA (dimensionality reduction)
- feature extraction

---

## Key Takeaways

- vectors → represent data
- matrices → represent datasets
- dot product → similarity
- eigenvalues → importance

---

## Mental Model

Linear Algebra answers:

👉 "How data is represented and transformed?"