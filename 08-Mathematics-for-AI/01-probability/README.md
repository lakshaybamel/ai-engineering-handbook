# Probability

Probability measures the **likelihood of an event occurring**.

It is the foundation of Machine Learning because:
- data is uncertain
- predictions are probabilistic
- models estimate likelihoods

---

## Basic Formula

```
P(Event) = (Number of favorable outcomes) / (Total outcomes)
```

Example:

- Tossing a coin → P(Head) = 1/2

---

## Types of Events

### Independent Events

One event does not affect the other.

Example:

- Tossing a coin twice

```
P(A and B) = P(A) * P(B)
```

### Dependent Events

One event affects another.

Example:

- Drawing cards without replacement

---

## Complementary Rule

Probability of event NOT happening:

```
P(A') = 1 - P(A)
```

Example:<br>
If P(rain) = 0.3<br>
Then P(no rain) = 0.7

---

## Addition Rule

### For mutually exclusive events:

```
P(A ∪ B) = P(A) + P(B)
```

Example:<br>
Getting 1 or 2 on dice

### For non-mutually exclusive events:

```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```

---

## Multiplication Rule

```
P(A ∩ B) = P(A) * P(B)
```

Used for independent events.

---

## Conditional Probability

Probability of A given B:

```
P(A | B) = P(A ∩ B) / P(B)
```

Example:<br>
Probability of disease given symptoms

---

## Law of Total Probability

Used when multiple conditions exist.

```
P(A) = P(A|B1)P(B1) + P(A|B2)P(B2) + ...
```

---

## Bayes Theorem (Very Important 🔥)

```
P(A | B) = [P(B | A) * P(A)] / P(B)
```

Used to update probability based on new evidence.

---

## Example (ML Context)

- A = spam email
- B = contains word "offer"

```
P(spam | offer)
```

Used in:

- Naive Bayes classifier
- spam detection
- medical diagnosis

---

## Practice Thinking

- Probability = uncertainty handling
- Conditional probability = learning from data
- Bayes = updating belief

---

## Mental Model

Machine Learning models answer:

👉 “What is the probability of this output given input?”

---

## Where It Is Used in ML

- Naive Bayes Algorithm
- Logistic Regression (probability output)
- Classification problems
- Risk prediction systems