# NumPy Quick Reference

A compact guide for quick revision of commonly used NumPy operations.

---

## 1. Import & Basics

Standard import:

```python
import numpy as np
```

Check version:

```python
np.__version__
```

Create simple array:

```python
arr = np.array([1,2,3,4])
print(arr)
```

NumPy arrays are faster than Python lists because they store elements in contiguous memory.

---

## 2. Creating Arrays

### From Python Lists

```python
np.array([1,2,3])
np.array([[1,2,3],[4,5,6]])
```

### Built-in Creators

```python
np.zeros(5)
np.ones((2,3))
np.full((2,2),7)
np.eye(3)
```

### Range Based

```python
np.arange(0,10,2)
np.linspace(0,1,5)
```
### Random Arrays

```python
np.random.rand(3,3)
np.random.randn(3,3)
np.random.randint(1,10,(2,2))
```

#### Set seed (reproducibility):

```python
np.random.seed(42)
```

---

## 3. Array Properties

Get structural information about the array:

```python
arr.shape     # dimensions (rows, columns)
arr.size      # total number of elements
arr.ndim      # number of dimensions
arr.dtype     # data type of elements
arr.itemsize  # bytes per element
arr.nbytes    # total memory used
```

Example:

```python
arr = np.array([[1,2,3],[4,5,6]])

print(arr.shape)
print(arr.ndim)
print(arr.size)
```

---

## 4. Data Types & Conversion

Check data type:

```python
arr.dtype
```

Convert data type:

```python
arr.astype(np.float64)
arr.astype(int)
arr.astype(bool)
```

Common NumPy data types:

```go
int32
int64
float32
float64
bool
```

Create array with specific dtype:

```python
np.array([1,2,3], dtype=np.float32)
```

---

## 5. Reshaping & Transformations

Change shape without changing data:

```python
arr.reshape(3,4)
arr.reshape(-1,2)   # auto calculate dimension
```

Flatten array:

```python
arr.flatten()   # returns copy
arr.ravel()     # returns view (faster)
```

Transpose (swap rows & columns):

```python
arr.T
np.transpose(arr)
```

Add or remove dimensions:

```python
arr.reshape(1,-1)   # row vector
arr.reshape(-1,1)   # column vector
```

---

## 6. Indexing & Slicing

### Basic Indexing

```python
arr[0]
arr[-1]
matrix[1,2]
```

### Slicing

```python
arr[1:4]
arr[:3]
arr[::2]

matrix[:,1]   # column
matrix[1,:]   # row
```

### Boolean Indexing

```python
arr[arr > 10]
arr[arr % 2 == 0]
```

### Fancy Indexing

```python
arr[[0,2,4]]
matrix[[0,2], :]
```

---

## 7. Copy vs View

View → shares memory  
Copy → new independent memory

Create view:

```python
b = a.view()
```

Create copy:

```python
c = a.copy()
```

Example:

```python
a = np.array([1,2,3])
b = a.view()
b[0] = 99

print(a)   # also changes
print(b)
```

Copy example:

```python
c = a.copy()
c[1] = 100

print(a)   # unchanged
print(c)
```

---


## 8. Vectorization

Operations applied element-wise automatically.

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

a + b
a * b
a ** 2
```

Scalar operations:

```python
a + 10
a * 5
```

No loops needed → faster execution

---

## 9. Broadcasting

Allows operations between arrays of different shapes.

Rule:
Dimensions must match OR one dimension must be 1.

Example:

```python
matrix = np.array([[1,2,3],
                   [4,5,6]])

vector = np.array([10,20,30])

matrix + vector
```

Another example:

```python
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])

a + b
```

Used heavily in ML for feature scaling.

---

## 10. Mathematical Operations

Element-wise operations:

```python
np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)
np.power(a,2)
```

Math functions:

```python
np.sqrt(a)
np.exp(a)
np.log(a)
np.abs(a)
np.round(a)
```

Trigonometric:

```python
np.sin(a)
np.cos(a)
np.tan(a)
```

---

## 11. Aggregations & Statistics

Basic statistics:

```python
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
```

Min & Max:

```python
np.min(arr)
np.max(arr)
np.argmin(arr)
np.argmax(arr)
```

Sum & Product:

```python
np.sum(arr)
np.prod(arr)
```

Axis based operations:

```python
np.sum(arr, axis=0)   # column-wise
np.sum(arr, axis=1)   # row-wise

np.mean(arr, axis=0)
np.mean(arr, axis=1)
```

---

## 12. Sorting & Searching

Sorting:

```python
np.sort(arr)
np.argsort(arr)
```

Searching:

```python
np.where(arr > 5)
np.searchsorted(arr, 5)
```

Condition checking:

```python
np.any(arr > 10)
np.all(arr > 0)
```

---

## 13. Unique & Counting

Unique elements:

```python
np.unique(arr)
```

Unique with counts:

```python
values, counts = np.unique(arr, return_counts=True)
```

Count non-zero:

```python
np.count_nonzero(arr)
```

Histogram (frequency distribution):

```python
np.bincount(arr)
```

---

## 14. Linear Algebra (basic)

Dot product:

```python
np.dot(a,b)
a @ b
```

Matrix multiplication:

```python
np.matmul(a,b)
```

Determinant:

```python
np.linalg.det(a)
```

Inverse:

```python
np.linalg.inv(a)
```

Eigenvalues & Eigenvectors:

```python
np.linalg.eig(a)
```

Norm (vector magnitude):

```python
np.linalg.norm(a)
```

---

## 15. Random Module

Random numbers:

```python
np.random.rand(3,3)        # uniform [0,1)
np.random.randn(3,3)       # normal distribution
np.random.randint(1,10,(2,2))
```

Random choice:

```python
np.random.choice([1,2,3,4], size=5)
```

Shuffle:

```python
arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
```

Set seed (reproducibility):

```python
np.random.seed(42)
```

Generate normal distribution:

```python
np.random.normal(loc=0, scale=1, size=10)
```