# Statistics for AI/ML

Statistics helps us understand data.

In Machine Learning:
- data → numbers
- numbers → patterns
- statistics → understanding those patterns

---

## Why Statistics is Important in AI

Used for:
- data analysis (EDA)
- feature understanding
- distribution checking
- model evaluation

---

## Random Variables

A random variable represents a numerical outcome of an experiment.

Types:

- Discrete → countable (e.g., number of students)
- Continuous → measurable (e.g., height, weight)

---

## Measures of Central Tendency

These describe the "center" of data.

---

### Mean (Average)

```
mean = sum(data) / len(data)
```

- sensitive to outliers

---

### Median

Middle value after sorting.

- robust to outliers

---

### Mode

Most frequent value.

---

### ML Insight

- Mean → used in normalization
- Median → used in missing value handling
- Mode → used for categorical data

---

## Measures of Dispersion

These describe spread of data.

---

### Variance

```
variance = Σ(x - mean)² / n
```

Measures how far values are from mean.

---

### Standard Deviation

```
std = √variance
```

easier to interpret than variance

---

### ML Insight

- high variance → data spread out
- low variance → data concentrated
- used in feature scaling

---

## Probability Distributions

Describe how data is distributed.

---

### Binomial Distribution

- fixed number of trials
- success/failure outcome

Example:

- coin toss

---

### Uniform Distribution

- all values equally likely

Example:

- random number generator

---

### Normal Distribution (Most Important)

Bell-shaped curve.

Properties:

- mean = median = mode

- symmetric

```
        ^
       / \
      /   \
     /     \
```

---

## ML Insight

- many real-world data follow normal distribution
- used in:
    - statistics
    - hypothesis testing
    - ML assumptions

---

## Key Takeaways

- mean → central value
- variance → spread
- distributions → shape of data

---

## Mental Model

Statistics answers:

👉 "What does the data look like?"

Before building models, always:

- check distribution
- check spread
- check central tendency