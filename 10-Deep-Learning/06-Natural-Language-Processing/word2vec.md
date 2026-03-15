# 🧠 Word2Vec

## 📌 Overview

**Word2Vec** is a technique used in **Natural Language Processing (NLP)** to convert words into **dense numerical vectors called word embeddings**.

Unlike traditional text representation methods such as **Bag of Words (BoW)** or **TF-IDF**, Word2Vec captures **semantic relationships between words**.

This means that words with similar meanings will have **similar vector representations**.

Word2Vec was introduced by **Google researchers in 2013** and became one of the most important methods for **learning word embeddings**.

---

## 🧠 Intuition

Traditional text representations treat words as **independent features**.

Example vocabulary:

```text
king
queen
man
woman
apple
car
```

In Bag of Words or TF-IDF:

* each word is treated independently
* no relationship between words is captured

However, Word2Vec learns **relationships between words based on context**.

Example relationships learned by Word2Vec:

```text
king - man + woman ≈ queen
```

This means the model understands **semantic similarities between words**.

---

## 📊 Word Embeddings

Word2Vec represents each word as a **vector in a continuous vector space**.

Example representation:

```text
king   → [0.21, -0.43, 0.76, ...]
queen  → [0.20, -0.40, 0.74, ...]
apple  → [-0.11, 0.58, -0.33, ...]
```

Words with similar meanings are located **close to each other in vector space**.

Example:

```text
king  → close to → queen
car   → close to → vehicle
dog   → close to → puppy
```

This property helps deep learning models understand **semantic relationships in language**.

---

## ⚙️ How Word2Vec Works

Word2Vec is trained using a **neural network** that learns word relationships from large text datasets.

The idea is simple:

```text
Words appearing in similar contexts tend to have similar meanings
```

Example sentence:

```text
"The cat is sitting on the mat"
```

Context words around **cat**:

```text
the, is, sitting
```

Word2Vec learns that words appearing in similar contexts share **similar meanings**.

---

## 🧩 Word2Vec Architectures

Word2Vec has two main architectures.

---

## 1️⃣ Continuous Bag of Words (CBOW)

CBOW predicts a **target word from surrounding context words**.

Example sentence:

```text
"The cat sits on the mat"
```

Context words:

```text
The, sits, on
```

Prediction:

```text
cat
```

Flow:

```text
Context Words → Neural Network → Target Word
```

CBOW is usually **faster and works well with large datasets**.

---

## 2️⃣ Skip-Gram

Skip-Gram predicts **context words from a target word**.

Example:

Target word:

```text
cat
```

Predicted context words:

```text
The, sits, on
```

Flow:

```text
Target Word → Neural Network → Context Words
```

Skip-Gram works better when the dataset contains **rare words**.

---

## ⚙️ Word2Vec Training Process

The training process typically follows these steps:

```text
Large Text Corpus
      ↓
Extract Word Contexts
      ↓
Train Neural Network
      ↓
Learn Word Embeddings
```

The neural network learns to **adjust word vectors so that similar words appear close together** in vector space.

---

## 📊 Example Word Relationships

Word embeddings learned by Word2Vec can capture interesting relationships.

Examples:

```text
Paris  - France + Italy ≈ Rome
```

```text
king - man + woman ≈ queen
```

This shows that Word2Vec captures **semantic and syntactic relationships**.

---

## ⚙️ Word2Vec in Python

Word2Vec can be implemented using the **Gensim library**.

Example:

```python
from gensim.models import Word2Vec

sentences = [
    ["i", "love", "machine", "learning"],
    ["deep", "learning", "is", "powerful"],
    ["machine", "learning", "is", "fun"]
]

model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)

vector = model.wv["learning"]

print(vector)
```

Output:

```text
Vector representation of the word "learning"
```

---

## 🚀 Advantages of Word2Vec

Word2Vec has several advantages over traditional methods.

### Captures Semantic Meaning

Words with similar meanings are represented by **similar vectors**.

---

### Dense Representation

Unlike sparse vectors in TF-IDF, Word2Vec produces **compact dense vectors**.

---

### Captures Word Relationships

Word2Vec can capture **semantic relationships between words**.

---

## ⚠️ Limitations of Word2Vec

Despite its advantages, Word2Vec also has limitations.

### Context Limitation

Each word has **only one embedding**, regardless of context.

Example:

```text
bank (river bank)
bank (financial bank)
```

Word2Vec cannot distinguish these meanings.

---

### Requires Large Datasets

Word2Vec performs best when trained on **large text corpora**.

---

## 📌 Word2Vec vs TF-IDF

| Feature                | TF-IDF         | Word2Vec      |
| ---------------------- | -------------- | ------------- |
| Representation         | Sparse vectors | Dense vectors |
| Semantic understanding | No             | Yes           |
| Word relationships     | No             | Yes           |
| Context awareness      | Limited        | Better        |

---

## 🚀 Modern Successors

Word2Vec inspired many modern embedding techniques.

Examples include:

* **GloVe**
* **FastText**
* **BERT**
* **Transformer-based embeddings**

These models capture **even deeper language understanding**.

---

## 🧠 One-Line Summary

> Word2Vec converts words into dense numerical vectors that capture semantic relationships, allowing machine learning models to understand similarities between words.
