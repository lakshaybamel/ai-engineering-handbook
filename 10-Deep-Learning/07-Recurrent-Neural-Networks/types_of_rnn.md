# 🔁 Types of Recurrent Neural Networks (RNN)

## 📌 Overview

Recurrent Neural Networks (RNNs) are designed to process **sequential data**, where the order of inputs matters.

Different tasks require **different input-output structures**, so RNNs can be organized into several architectural types depending on how **inputs and outputs are arranged over time**.

These architectures allow RNNs to handle various problems such as:

* text classification
* machine translation
* speech recognition
* time series forecasting

---

## 🧠 Intuition

Unlike traditional neural networks that process **fixed-size inputs and outputs**, RNNs can process **sequences of varying lengths**.

Example sequence:

```text
I → love → deep → learning
```

Each word is processed **one time step at a time**, allowing the network to maintain **context across the sequence**.

Depending on the task, the model may produce:

* a single output
* an output at each time step
* another sequence

This leads to different **RNN architectures**.

---

## 🧩 Common Types of RNN Architectures

There are several common RNN structures.

---

## 1️⃣ One-to-One

This is the **standard neural network structure**.

```text
Input → Output
```

Example:

```text
Image → Label
```

Applications:

* image classification
* regression problems

This architecture is **not specific to RNNs** but is included for comparison.

---

## 2️⃣ One-to-Many

A single input produces a **sequence of outputs**.

Structure:

```text
Input → Output₁ → Output₂ → Output₃
```

Example:

```text
Image → Generate description
```

Example output:

```text
"A dog running in the park"
```

Applications:

* **image captioning**
* music generation

---

## 3️⃣ Many-to-One

A sequence of inputs produces **one output**.

Structure:

```text
Input₁ → Input₂ → Input₃ → Output
```

Example:

```text
"This movie is amazing" → Positive
```

Applications:

* **sentiment analysis**
* text classification
* spam detection

This is one of the **most common RNN architectures**.

---

## 4️⃣ Many-to-Many (Same Length)

A sequence of inputs produces a **sequence of outputs of the same length**.

Structure:

```text
Input₁ → Output₁
Input₂ → Output₂
Input₃ → Output₃
```

Example:

```text
Word tagging (Part-of-Speech tagging)
```

Example sentence:

```text
Dogs bark loudly
```

Output tags:

```text
Noun Verb Adverb
```

Applications:

* **part-of-speech tagging**
* named entity recognition

---

## 5️⃣ Many-to-Many (Different Length)

A sequence of inputs produces a **sequence of outputs with different length**.

Structure:

```text
Input Sequence → Encoder → Decoder → Output Sequence
```

Example:

```text
English → French translation
```

Example:

```text
Input:
"I love machine learning"
```

Output:

```text
"J'aime l'apprentissage automatique"
```

Applications:

* **machine translation**
* speech recognition
* chatbot systems

This architecture is commonly called the **Encoder–Decoder model**.

---

## 📊 Summary of RNN Types

| Architecture                    | Input    | Output   | Example Application  |
| ------------------------------- | -------- | -------- | -------------------- |
| One-to-One                      | Single   | Single   | Image classification |
| One-to-Many                     | Single   | Sequence | Image captioning     |
| Many-to-One                     | Sequence | Single   | Sentiment analysis   |
| Many-to-Many (same length)      | Sequence | Sequence | POS tagging          |
| Many-to-Many (different length) | Sequence | Sequence | Machine translation  |

---

## ⚙️ Visual Example

Example sentence:

```text
"I love deep learning"
```

Many-to-One example:

```text
I → love → deep → learning → Positive Sentiment
```

Many-to-Many example:

```text
I → Pronoun
love → Verb
deep → Adjective
learning → Noun
```

---

## ⚠️ Important Points

* RNN architectures vary depending on **input-output sequence structure**.
* Many-to-One architecture is commonly used for **sentiment analysis**.
* Many-to-Many architectures are used in **translation and tagging tasks**.
* Encoder–Decoder architectures allow handling **different input and output lengths**.

---

## 🧠 One-Line Summary

> Different RNN architectures handle different sequence tasks by organizing inputs and outputs across time steps, enabling applications such as sentiment analysis, translation, and sequence labeling.
