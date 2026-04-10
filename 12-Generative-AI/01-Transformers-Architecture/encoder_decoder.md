# Encoder & Decoder in Transformers

## 🚀 Introduction

The Transformer architecture is built using two main components:

* **Encoder** → understands input
* **Decoder** → generates output

👉 Together, they enable tasks like:

* Translation
* Summarization
* Text generation

---

## 🧠 Simple Intuition

Think of it like:

* Encoder → *“Read and understand the sentence”*
* Decoder → *“Write the output based on understanding”*

---

## 🏗️ Encoder Overview

### 📌 Role

* Takes input sequence
* Converts it into a meaningful representation

---

### ⚙️ Encoder Flow

1. Input text → tokens
2. Tokens → embeddings
3. Add positional encoding
4. Pass through multiple encoder layers

---

### 🔹 Inside Each Encoder Layer

Each layer has:

#### 1. Self-Attention

* Each word looks at all other words
* Captures relationships

---

#### 2. Feed Forward Network (FNN)

* Processes each token independently
* Adds non-linearity

---

#### 3. Residual Connection + Layer Norm

* Stabilizes training
* Helps deep networks learn better

---

### 📊 Output of Encoder

👉 A **context-rich representation** of the input
👉 Passed to the decoder

---

## 🏗️ Decoder Overview

### 📌 Role

* Generates output sequence step-by-step

---

### ⚙️ Decoder Flow

1. Takes previous output tokens
2. Uses encoder output
3. Predicts next token

---

### 🔹 Inside Each Decoder Layer

Each layer has:

#### 1. Masked Self-Attention

* Prevents seeing future words
* Ensures correct sequence generation

---

#### 2. Cross-Attention

* Connects decoder with encoder output
* Helps focus on relevant input parts

---

#### 3. Feed Forward Network (FNN)

* Further processes the data

---

#### 4. Residual + Layer Norm

* Improves training stability

---

## 🔄 How Encoder & Decoder Work Together

### Step-by-step:

1. Encoder processes full input
2. Creates contextual representation
3. Decoder:

   * Takes previous outputs
   * Looks at encoder output
   * Predicts next word
4. Repeat until sequence ends

---

## 📌 Example (Translation)

**Input:**

```id="4q0u1l"
Hello world
```

### Encoder:

* Understands meaning of sentence

---

### Decoder:

* Generates:

```id="eqz7rk"
Bonjour le monde
```

👉 Step-by-step generation

---

## 📊 Encoder vs Decoder

| Feature   | Encoder                | Decoder                  |
| --------- | ---------------------- | ------------------------ |
| Role      | Understand input       | Generate output          |
| Attention | Self-attention         | Masked + Cross-attention |
| Input     | Full sequence          | Previous outputs         |
| Output    | Context representation | Final prediction         |

---

## 🔥 Key Differences

* Encoder sees **entire input at once**
* Decoder generates **one token at a time**
* Decoder uses **masking + encoder information**

---

## ⚠️ Important Notes

* Some models use only encoder (e.g., classification tasks)
* Some use only decoder (e.g., GPT-like models)
* Full encoder-decoder used in:

  * Translation
  * Summarization

---

## 🎯 Interview Key Points

* Encoder → context understanding
* Decoder → sequence generation
* Decoder uses:

  * Masked self-attention
  * Cross-attention
* Encoder output is passed to decoder
* Used in sequence-to-sequence tasks

---

## 🧠 One-Line Summary

> The encoder understands the input sequence, and the decoder generates the output sequence using that understanding.

---

## 🔚 Final Thought

The encoder-decoder design enables transformers to **learn relationships and generate meaningful sequences**, making them powerful for real-world NLP tasks.
