# 📊 TF-IDF (Term Frequency – Inverse Document Frequency)

## 📌 Overview

**TF-IDF** is a statistical technique used in **Natural Language Processing (NLP)** to measure how important a word is in a document relative to a collection of documents.

It is widely used for:

* text classification
* information retrieval
* search engines
* sentiment analysis

TF-IDF improves upon the **Bag of Words (BoW)** approach by giving **higher importance to informative words** and reducing the importance of very common words.

---

## 🧠 Intuition

Consider two documents:

```text
Document 1: I love machine learning
Document 2: I love deep learning
```

Common words like:

```text
I
love
learning
```

appear frequently in both documents.

However, words like:

```text
machine
deep
```

provide more **unique information** about the document.

TF-IDF helps assign **higher weights to important words** and lower weights to common words.

---

## 🧩 Components of TF-IDF

TF-IDF is composed of two parts:

1️⃣ **Term Frequency (TF)**
2️⃣ **Inverse Document Frequency (IDF)**

---

## 1️⃣ Term Frequency (TF)

Term Frequency measures how often a word appears in a document.

Formula:

```text
TF(word) = Number of times the word appears in a document
           ------------------------------------------------
           Total number of words in the document
```

Example document:

```text
"I love machine learning because machine learning is powerful"
```

Word counts:

```text
machine → 2
learning → 2
love → 1
```

If total words = 8

Example:

```text
TF(machine) = 2 / 8 = 0.25
```

This tells us **how important a word is within a single document**.

---

## 2️⃣ Inverse Document Frequency (IDF)

Some words appear in many documents, which makes them less useful.

Examples:

```text
the
is
and
a
```

IDF reduces the importance of such frequently occurring words.

Formula:

```text
IDF(word) = log(Total number of documents / Number of documents containing the word)
```

Example:

Total documents:

```text
100
```

Word "machine" appears in:

```text
10 documents
```

Then:

```text
IDF(machine) = log(100 / 10)
             = log(10)
```

If a word appears in **many documents**, its IDF value becomes **small**.

If a word appears in **few documents**, its IDF value becomes **large**.

---

## ⚙️ TF-IDF Calculation

TF-IDF combines both TF and IDF.

Formula:

```text
TF-IDF = TF × IDF
```

Example:

```text
TF(machine) = 0.25
IDF(machine) = 1.0
```

Then:

```text
TF-IDF(machine) = 0.25 × 1.0 = 0.25
```

Words with higher TF-IDF values are considered **more important**.

---

## 📊 Example TF-IDF Representation

Example sentences:

```text
Sentence 1: I love machine learning
Sentence 2: I love deep learning
```

Vocabulary:

```text
I
love
machine
deep
learning
```

TF-IDF matrix example:

| Word     | Sentence 1 | Sentence 2 |
| -------- | ---------- | ---------- |
| I        | low        | low        |
| love     | low        | low        |
| machine  | high       | 0          |
| deep     | 0          | high       |
| learning | medium     | medium     |

This matrix converts text into **numerical vectors**.

---

## ⚙️ TF-IDF in Python

TF-IDF can easily be implemented using **scikit-learn**.

Example:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love machine learning",
    "I love deep learning"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

Output:

* list of vocabulary words
* TF-IDF numerical matrix

This matrix can be used as input for **machine learning models**.

---

## 🚀 Advantages of TF-IDF

TF-IDF provides several benefits.

### Reduces Importance of Common Words

Common words receive **low weights**.

---

### Highlights Important Words

Words unique to a document receive **higher importance**.

---

### Efficient Text Representation

Transforms text into **numerical feature vectors**.

---

## ⚠️ Limitations of TF-IDF

Despite its usefulness, TF-IDF has some limitations.

### No Understanding of Word Meaning

TF-IDF does not understand semantic relationships.

Example:

```text
car
automobile
```

These words have similar meaning but TF-IDF treats them as **different words**.

---

### No Context Awareness

TF-IDF does not consider **word order or context**.

Example:

```text
I love dogs
Dogs love me
```

Both sentences may produce similar vectors.

---

## 📌 When TF-IDF is Used

TF-IDF is commonly used in:

* document classification
* search engines
* spam detection
* information retrieval systems

It is often used before applying models like:

* Logistic Regression
* Naive Bayes
* Support Vector Machines

---

## 🧠 One-Line Summary

> TF-IDF is a technique that converts text into numerical vectors by measuring how important a word is in a document relative to a collection of documents.
