# Masked Attention in Transformers

## 🚀 Introduction

**Masked Attention** is a special type of self-attention used in the **decoder** of transformers.

👉 It ensures that:

> The model can only see **past tokens**, not future ones

---

## 🧠 Simple Intuition

When generating text:

* You write word by word
* You don’t know future words

👉 Masked attention enforces this behavior in the model.

---

## 📌 Why Do We Need Masking?

Without masking:

* The model could “peek” at future words
* This would make training unrealistic

👉 Masking ensures:

* Proper sequence generation
* Real-world behavior during training

---

## ⚙️ How Masked Attention Works

It is similar to self-attention, but:

👉 Future positions are **blocked (masked)**

---

### 🔒 Masking Concept

For a sequence:

```id="j9g6uh"
I love AI
```

While predicting “love”:

* Allowed → “I”
* Blocked → “AI”

---

## 🔄 Step-by-Step

1. Compute attention scores
2. Apply mask:

   * Future positions → set to -∞
3. Apply softmax
4. Future tokens get zero probability

---

## 📊 Mask Matrix Example

```id="y5a8zb"
[1 0 0]
[1 1 0]
[1 1 1]
```

👉 1 = allowed
👉 0 = masked

---

## 🧩 Where It Is Used

In decoder layer:

1. **Masked Self-Attention** ✅
2. Cross-Attention
3. Feed Forward Network

---

## 🔥 Why Masked Attention is Important

| Feature               | Benefit                     |
| --------------------- | --------------------------- |
| Prevents cheating     | No future information       |
| Sequential generation | Mimics real text generation |
| Stable training       | Consistent behavior         |

---

## ⚠️ Important Notes

* Used only in **decoder**
* Not needed in encoder (encoder sees full input)
* Essential for:

  * Language models
  * Text generation

---

## 🎯 Interview Key Points

* Masked attention blocks future tokens
* Used in decoder self-attention
* Ensures left-to-right generation
* Implemented using mask matrix
* Prevents information leakage

---

## 🧠 One-Line Summary

> Masked attention ensures the model only attends to past tokens, preventing it from seeing future information during generation.

---

## 📌 Quick Analogy

Think of writing a sentence:

* You can only use words you’ve already written
* You cannot see future words

👉 That restriction = masked attention

---

## 🔚 Final Thought

Masked attention is crucial for making transformers behave like real sequence generators, ensuring **correct and realistic text generation**.
