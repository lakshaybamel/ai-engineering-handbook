# Static vs Contextual Embeddings

## 🚀 What are Embeddings?

**Embeddings** are numerical representations of words (or text) in vector form.

👉 They convert text into numbers so that models can understand and process it.

---

## 🧠 Simple Intuition

Think of embeddings as:

> 🧭 A way to place words in a space where similar words are closer together

### Example:

* “king” and “queen” → close
* “king” and “apple” → far

---

## 🔤 Why Do We Need Embeddings?

Computers cannot understand raw text.

So we convert:

```
"dog" → [0.21, -0.45, 0.78, ...]
```

👉 This vector captures meaning and relationships.

---

# 🧩 Types of Embeddings

There are two main types:

1. **Static Embeddings**
2. **Contextual Embeddings**

---

# 🔹 1. Static Embeddings

## 📌 Definition

Static embeddings assign **one fixed vector** to each word, regardless of context.

---

## ⚙️ Examples

* Word2Vec
* GloVe
* FastText

---

## 🧠 Example

Word: **“bank”**

* “river bank”
* “bank account”

👉 Static embedding:

```
bank → same vector in both cases ❌
```

---

## ✅ Advantages

* Simple and fast
* Pre-computed (no need to train every time)
* Less computational cost

---

## ❌ Limitations

* Cannot capture context
* Same meaning for different usages
* Struggles with ambiguity

---

# 🔹 2. Contextual Embeddings

## 📌 Definition

Contextual embeddings generate **different vectors for the same word depending on context**.

---

## ⚙️ Examples

* BERT
* GPT
* Transformer-based models

---

## 🧠 Example

Word: **“bank”**

* “river bank” → vector A
* “bank account” → vector B

👉 Different meanings → different embeddings ✅

---

## ✅ Advantages

* Captures context
* Handles ambiguity
* Much better performance in NLP tasks

---

## ❌ Limitations

* Computationally expensive
* Requires powerful models

---

# 📊 Static vs Contextual (Comparison)

| Feature           | Static Embeddings | Contextual Embeddings |
| ----------------- | ----------------- | --------------------- |
| Vector per word   | One fixed vector  | Dynamic vectors       |
| Context awareness | ❌ No              | ✅ Yes                 |
| Example           | Word2Vec          | BERT, GPT             |
| Performance       | Basic             | Advanced              |
| Compute cost      | Low               | High                  |

---

# 🔥 Why Contextual Embeddings Matter

Modern NLP tasks require understanding meaning in context:

* Chatbots
* Translation
* Summarization
* Question answering

👉 Static embeddings are not enough.

---

# 🧠 Role in Transformers & LLMs

* Transformers use **contextual embeddings**
* Each word representation changes based on:

  * Surrounding words
  * Sentence meaning

👉 This is why LLMs sound “intelligent”

---

# 🎯 Interview Key Points

* Embeddings convert text → vectors
* Static embeddings:

  * One vector per word
  * No context awareness
* Contextual embeddings:

  * Dynamic vectors
  * Context-aware
* Modern models (LLMs) use **contextual embeddings**

---

# 🧠 One-Line Summary

> Static embeddings give fixed word vectors, while contextual embeddings adapt word meaning based on context.

---

# 📌 Quick Example

Sentence 1:

```
He sat on the bank of the river
```

Sentence 2:

```
She deposited money in the bank
```

👉 Contextual embeddings:

* “bank” → different meanings
* → different vectors

---

# 🔚 Final Thought

The shift from **static → contextual embeddings** is one of the biggest breakthroughs in NLP, enabling models to truly understand language context.
