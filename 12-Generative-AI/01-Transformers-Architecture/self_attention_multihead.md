# Self-Attention & Multi-Head Attention

## 🚀 Introduction

**Self-Attention** and **Multi-Head Attention** are key components of the Transformer architecture.

👉 They allow the model to:

* Understand relationships between words
* Capture context effectively
* Focus on important parts of a sentence

---

# 🧠 1. Self-Attention

## 📌 Definition

**Self-Attention** is a mechanism where:

> Each word in a sentence looks at every other word and decides how important they are.

---

## 🧠 Simple Intuition

When you read a sentence:

* You don’t process each word independently
* You relate words with each other

👉 Self-attention does the same.

---

## 📌 Example

Sentence:

```
The animal didn’t cross the street because it was too tired
```

👉 Word **“it”**:

* Looks at all words
* Finds “animal” is most relevant

---

## ⚙️ How Self-Attention Works

For each word:

1. Create:

   * Query (Q)
   * Key (K)
   * Value (V)

2. Compute attention scores

3. Apply softmax (convert to probabilities)

4. Multiply with values

5. Get final representation

👉 Output = context-aware word representation

---

## 🔥 Key Benefit

* Captures relationships between words
* Handles long-distance dependencies

---

# 🧠 2. Multi-Head Attention

## 📌 Definition

**Multi-Head Attention** means:

> Running multiple self-attention mechanisms in parallel.

---

## 🧠 Simple Intuition

Instead of looking at one relationship:

👉 Look at **multiple perspectives simultaneously**

---

## 📌 Example

Sentence:

```
The cat sat on the mat
```

Different attention heads may focus on:

* Subject → “cat”
* Action → “sat”
* Location → “mat”

---

## ⚙️ How It Works

1. Split embeddings into multiple parts
2. Apply self-attention independently (multiple heads)
3. Combine outputs
4. Pass through a linear layer

---

## 📊 Why Multi-Head Attention?

| Feature              | Benefit                         |
| -------------------- | ------------------------------- |
| Multiple views       | Capture different relationships |
| Better understanding | Richer representations          |
| Parallel processing  | Efficient computation           |

---

## 🔄 Self-Attention vs Multi-Head

| Feature        | Self-Attention | Multi-Head Attention |
| -------------- | -------------- | -------------------- |
| Heads          | Single         | Multiple             |
| Perspective    | One            | Many                 |
| Performance    | Good           | Better               |
| Representation | Limited        | Rich                 |

---

## 🔥 Role in Transformers

* Used in:

  * Encoder (self-attention)
  * Decoder (self + cross attention)
* Core building block of LLMs

---

## ⚠️ Limitations

* High computational cost
* Memory intensive for long sequences

---

## 🎯 Interview Key Points

* Self-attention:

  * Each word attends to all others
  * Uses Q, K, V

* Multi-head attention:

  * Multiple attention heads in parallel
  * Captures different relationships

* Improves model performance significantly

---

## 🧠 One-Line Summary

> Self-attention captures relationships between words, while multi-head attention enhances it by learning multiple relationships in parallel.

---

## 📌 Quick Analogy

Think of analyzing a sentence:

* Self-attention → One person analyzing
* Multi-head → Multiple experts analyzing different aspects

👉 Combined result = better understanding

---

## 🔚 Final Thought

Self-attention gives transformers their ability to **understand context**, and multi-head attention makes that understanding **richer and more powerful**.
