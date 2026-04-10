# Feed Forward Network (FNN) in Transformers

## 🚀 Introduction

The **Feed Forward Network (FNN)** is a key component in each transformer layer.

👉 It is applied **after the attention mechanism** to further process the information.

---

## 🧠 Simple Intuition

Think of it like:

> Attention finds *what is important*, and FNN processes *how to transform that information*.

---

## 📌 Where It Is Used

In each transformer layer:

* After **Self-Attention / Multi-Head Attention**
* Present in both:

  * Encoder
  * Decoder

---

## ⚙️ Structure of Feed Forward Network

The FNN is a **simple fully connected neural network** applied to each token independently.

### Basic Form:

```
FNN(x) = max(0, xW₁ + b₁)W₂ + b₂
```

👉 Two linear layers with an activation function in between

---

## 🔄 Step-by-Step Flow

1. Input vector comes from attention layer
2. First linear transformation
3. Apply activation function (ReLU)
4. Second linear transformation
5. Output passed to next layer

---

## 🧩 Key Characteristics

### 🔹 Position-wise

* Applied independently to each token
* No interaction between tokens here

---

### 🔹 Same Weights

* Same network used for all tokens

---

### 🔹 Non-Linearity

* Adds complexity using activation function

---

## 📌 Example (Intuition)

After attention:

* Model knows:

  * “cat” is subject
  * “sat” is action

👉 FNN:

* Refines this representation
* Makes it more useful for next layer

---

## 📊 Why FNN is Important

| Feature                | Benefit                 |
| ---------------------- | ----------------------- |
| Non-linearity          | Learns complex patterns |
| Token-wise processing  | Efficient               |
| Feature transformation | Improves representation |

---

## 🔥 Role in Transformers

Each transformer layer consists of:

1. Attention mechanism
2. Feed Forward Network

👉 Both are essential:

* Attention → relationships
* FNN → transformation

---

## ⚠️ Important Note

FNN is combined with:

* **Residual Connections**
* **Layer Normalization**

👉 Ensures stable training

---

## 🎯 Interview Key Points

* FNN = two linear layers + activation
* Applied **after attention**
* Works **independently on each token**
* Adds non-linearity
* Present in both encoder and decoder

---

## 🧠 One-Line Summary

> Feed Forward Network processes each token independently after attention to transform features and add non-linearity.

---

## 📌 Quick Analogy

Think of it like:

* Attention → finds important information
* FNN → processes and refines that information

---

## 🔚 Final Thought

While attention captures relationships, the Feed Forward Network ensures the model can **learn complex transformations**, making transformers powerful and expressive.
