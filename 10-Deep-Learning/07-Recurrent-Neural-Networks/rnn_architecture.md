# 🔁 Recurrent Neural Network (RNN) Architecture

## 📌 Overview

A **Recurrent Neural Network (RNN)** is a type of neural network designed to process **sequential data**.

Unlike traditional neural networks that assume inputs are independent, RNNs can **remember previous information in a sequence**.

This makes them useful for tasks involving **ordered data**, such as:

* text processing
* speech recognition
* time series prediction
* language translation

RNNs achieve this by maintaining a **hidden state** that carries information from previous time steps.

---

## 🧠 Intuition

Consider the sentence:

```text
I love deep learning
```

When humans read this sentence, we understand each word by considering the **previous words**.

Example:

```text
"I" → starting context
"I love" → emotion detected
"I love deep learning" → full meaning
```

Traditional neural networks process inputs **independently**, but RNNs process inputs **step-by-step**, remembering previous context.

Example sequence processing:

```text
Word₁ → Word₂ → Word₃ → Word₄
```

Each step updates the **internal memory of the network**.

---

## 🧩 Why RNNs Are Needed

Standard neural networks struggle with **sequence-based data**.

Example problems:

### Language Modeling

Predict the next word:

```text
I love deep ______
```

Prediction:

```text
learning
```

---

### Sentiment Analysis

Classify text sentiment:

```text
"This movie was fantastic!"
```

Prediction:

```text
Positive
```

---

### Time Series Forecasting

Predict future values:

```text
Stock prices
Weather data
```

These tasks require understanding **temporal relationships**, which RNNs are designed for.

---

## ⚙️ RNN Architecture

An RNN processes data **one element at a time** while maintaining a hidden state.

Basic structure:

```text
Input → Hidden State → Output
```

However, unlike feedforward networks, the hidden state is **passed to the next step in the sequence**.

Flow:

```text
x₁ → RNN → h₁
x₂ → RNN → h₂
x₃ → RNN → h₃
```

Where:

* **xₜ** → input at time step t
* **hₜ** → hidden state at time step t

The hidden state carries information from **previous time steps**.

---

## 🔄 Unrolled RNN

Although an RNN is a single network, it is often visualized as **multiple time steps connected sequentially**.

Example:

```text
x₁ → [RNN] → h₁
           ↓
x₂ → [RNN] → h₂
           ↓
x₃ → [RNN] → h₃
           ↓
x₄ → [RNN] → h₄
```

This representation is called **unrolling the RNN through time**.

Each step shares the **same weights and parameters**.

---

## ⚙️ Mathematical Representation

The hidden state is computed using:

```text
hₜ = f(Wₓh xₜ + Wₕh hₜ₋₁ + b)
```

Where:

* **xₜ** → input at time t
* **hₜ₋₁** → previous hidden state
* **Wₓh** → input weights
* **Wₕh** → recurrent weights
* **b** → bias
* **f()** → activation function (usually tanh or ReLU)

The output is computed as:

```text
yₜ = Wₕy hₜ + b
```

---

## 🧠 Hidden State (Memory)

The **hidden state** is the key idea behind RNNs.

It acts as a **memory** that stores information from previous inputs.

Example:

```text
Input sequence:
"I love machine learning"
```

While processing:

* "I" → stored in memory
* "love" → context updated
* "machine" → context updated
* "learning" → full context available

This memory helps the network understand **relationships between words in a sentence**.

---

## 🚀 Advantages of RNNs

RNNs provide several advantages for sequence data.

### Handles Sequential Data

RNNs are specifically designed for **ordered data**.

---

### Context Awareness

They maintain a hidden state that captures **previous context**.

---

### Parameter Sharing

The same weights are reused across time steps, which reduces the **number of parameters**.

---

## ⚠️ Limitations of Basic RNNs

Despite their advantages, basic RNNs have several limitations.

### Vanishing Gradient Problem

Gradients may become extremely small during backpropagation, making it difficult to learn **long-term dependencies**.

---

### Difficulty Learning Long Sequences

Basic RNNs struggle with long sentences or sequences.

Example:

```text
"The movie I watched yesterday evening with my friends was absolutely fantastic"
```

The model may forget early words like:

```text
movie
```

before reaching the end of the sentence.

---

## 🚀 Improved RNN Variants

To address these limitations, improved architectures were developed.

Examples:

* **LSTM (Long Short-Term Memory)**
* **GRU (Gated Recurrent Unit)**

These models help capture **long-term dependencies in sequences**.

---

## ⚠️ Important Points

* RNNs are designed for **sequential data**.
* They maintain a **hidden state that acts as memory**.
* Information flows from **previous time steps to future steps**.
* Standard RNNs struggle with **long-term dependencies**.

---

## 🧠 One-Line Summary

> Recurrent Neural Networks process sequential data by maintaining a hidden state that carries information from previous inputs, allowing the network to capture temporal relationships in sequences.
