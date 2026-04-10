# Cross-Attention in Transformers

## 🚀 Introduction

**Cross-Attention** is a mechanism used in the **decoder** of transformers.

👉 It allows the decoder to:

> **Focus on relevant parts of the encoder output while generating text**

---

## 🧠 Simple Intuition

Think of it like:

* Encoder → understands the input
* Decoder → generates output

👉 Cross-attention helps the decoder:

> “Look back at the input and pick important information”

---

## 📌 Why Do We Need Cross-Attention?

While generating output:

* The decoder needs context from:

  * Previous generated words
  * Original input sentence

👉 Cross-attention connects **input (encoder)** with **output (decoder)**

---

## ⚙️ How Cross-Attention Works

It uses the same attention mechanism but with a twist:

| Component | Source  |
| --------- | ------- |
| Query (Q) | Decoder |
| Key (K)   | Encoder |
| Value (V) | Encoder |

---

## 🔄 Step-by-Step Flow

1. Decoder generates a Query (Q)
2. Encoder outputs provide Key (K) and Value (V)
3. Compute attention scores
4. Focus on important input tokens
5. Generate next output

---

## 📌 Example (Translation)

**Input (Encoder):**

```id="6iyrxt"
I love programming
```

---

**Output (Decoder):**

```id="4v6hru"
Je aime programmer
```

👉 While generating each word:

* Decoder looks at encoder output
* Focuses on relevant input words

---

## 🧩 Where It Fits in Decoder

Each decoder layer has:

1. Masked Self-Attention
2. **Cross-Attention**
3. Feed Forward Network

---

## 📊 Cross-Attention vs Self-Attention

| Feature      | Self-Attention         | Cross-Attention                  |
| ------------ | ---------------------- | -------------------------------- |
| Input source | Same sequence          | Different sequences              |
| Q, K, V      | From same input        | Q from decoder, K/V from encoder |
| Purpose      | Internal relationships | Connect input & output           |

---

## 🔥 Why It Is Important

* Enables sequence-to-sequence learning
* Helps in:

  * Translation
  * Summarization
  * Question answering

👉 Without cross-attention, decoder cannot use input effectively

---

## ⚠️ Important Notes

* Only used in **encoder-decoder models**
* Not used in decoder-only models (like GPT)

---

## 🎯 Interview Key Points

* Cross-attention connects encoder and decoder
* Query → decoder
* Key, Value → encoder
* Used in sequence generation tasks
* Helps decoder focus on relevant input

---

## 🧠 One-Line Summary

> Cross-attention allows the decoder to focus on relevant parts of the encoder output while generating each token.

---

## 📌 Quick Analogy

Think of translation:

* You read the original sentence
* While writing translation, you keep looking back

👉 That “looking back” = cross-attention

---

## 🔚 Final Thought

Cross-attention is what enables transformers to **link input understanding with output generation**, making tasks like translation and summarization possible.
