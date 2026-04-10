# Residual Connections in Transformers

## 🚀 Introduction

**Residual Connections (Skip Connections)** are used in transformers to:

* Improve training of deep networks
* Prevent loss of important information
* Help gradients flow easily

👉 They are essential for stable and efficient training.

---

## 🧠 Simple Intuition

Think of it like:

> Instead of completely transforming the input, also keep a direct path from input to output.

---

## 📌 Basic Idea

Instead of:

```
Output = Layer(x)
```

We use:

```
Output = Layer(x) + x
```

👉 Add original input back to the output

---

## 🔄 Why Do We Need Residual Connections?

Deep neural networks face problems like:

### ❌ Vanishing Gradient

* Gradients become very small
* Learning slows down

---

### ❌ Information Loss

* Original input gets distorted after many layers

---

### ✅ Residual Connections Solve This

* Preserve original information
* Improve gradient flow
* Enable deeper networks

---

## ⚙️ How It Works in Transformers

Each sub-layer (like attention or feed-forward) follows:

1. Apply operation (e.g., self-attention)
2. Add input (skip connection)
3. Apply Layer Normalization

---

### 📌 Structure

```
x → SubLayer → + → LayerNorm → Output
      ↑_______|
```

👉 The input “x” is added back

---

## 🧠 Example (Intuition)

Imagine:

* Input = important sentence meaning
* Layer modifies it

👉 Residual connection ensures:

* Original meaning is not lost

---

## 📊 Benefits

| Feature               | Benefit                      |
| --------------------- | ---------------------------- |
| Gradient flow         | Easier training              |
| Information retention | Preserves input              |
| Stability             | Reduces training issues      |
| Deep models           | Enables stacking many layers |

---

## 🔥 Where It Is Used

Residual connections are applied in:

* Self-attention layer
* Feed-forward network

👉 Used multiple times in both encoder and decoder

---

## ⚠️ Important Note

Residual connection is usually followed by:

* **Layer Normalization**

👉 Together they stabilize training

---

## 🎯 Interview Key Points

* Residual connection = `Output = Layer(x) + x`
* Helps prevent vanishing gradient
* Preserves input information
* Used in every transformer layer
* Combined with layer normalization

---

## 🧠 One-Line Summary

> Residual connections add the original input back to the output, helping transformers train deeper and more stable models.

---

## 📌 Quick Analogy

Think of learning:

* Instead of forgetting basics while learning advanced topics
* You keep basics + add new knowledge

👉 That’s residual connection.

---

## 🔚 Final Thought

Residual connections ensure that transformers **don’t forget important information while learning complex patterns**, making deep architectures practical.
