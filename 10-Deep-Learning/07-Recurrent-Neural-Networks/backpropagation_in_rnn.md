# 🔁 Backpropagation in Recurrent Neural Networks (RNN)

## 📌 Overview

Training a **Recurrent Neural Network (RNN)** involves updating the network’s weights so that it can learn patterns from sequential data.

Just like other neural networks, RNNs are trained using **backpropagation**.
However, because RNNs process **sequences over time**, a special technique called **Backpropagation Through Time (BPTT)** is used.

BPTT allows gradients to flow **backward through all time steps in the sequence**, enabling the network to learn from past inputs.

---

## 🧠 Intuition

Consider the sentence:

```text
"I love deep learning"
```

When processing this sentence, the RNN handles words sequentially:

```text
I → love → deep → learning
```

At each step:

* the model updates its **hidden state**
* the hidden state carries information from previous words

When the model makes a prediction and calculates the **loss**, the error must be propagated **back through every time step** to update the weights.

This process is called:

```text
Backpropagation Through Time (BPTT)
```

---

## 🔄 Unrolled RNN During Training

To understand BPTT, an RNN is often visualized as an **unrolled network across time steps**.

Example:

```text
x₁ → [RNN] → h₁ → y₁
           ↓
x₂ → [RNN] → h₂ → y₂
           ↓
x₃ → [RNN] → h₃ → y₃
```

Where:

* **xₜ** → input at time step t
* **hₜ** → hidden state at time step t
* **yₜ** → output at time step t

Even though it appears as multiple networks, **all time steps share the same weights**.

---

## ⚙️ Forward Pass in RNN

During the forward pass:

1. Input sequence is processed step by step.
2. Hidden states are updated.
3. Predictions are generated.
4. Loss is calculated.

Example sequence:

```text
x₁ → h₁
x₂ → h₂
x₃ → h₃
```

Hidden state calculation:

```text
hₜ = f(Wₓh xₜ + Wₕh hₜ₋₁ + b)
```

Output:

```text
yₜ = Wₕy hₜ
```

Loss is then calculated using predicted outputs and true labels.

---

## 🔙 Backpropagation Through Time (BPTT)

After computing the loss, gradients are propagated **backwards through all time steps**.

Example sequence:

```text
x₁ → x₂ → x₃ → x₄
```

During backpropagation:

```text
Loss → t₄ → t₃ → t₂ → t₁
```

The gradients flow **backward through time**, updating the shared weights.

This allows earlier time steps to influence learning.

---

## ⚙️ Gradient Flow in RNN

The gradient for weights depends on contributions from **all previous time steps**.

Example:

```text
Gradient(W) =
∂Loss/∂h₄ +
∂Loss/∂h₃ +
∂Loss/∂h₂ +
∂Loss/∂h₁
```

This cumulative gradient helps the network **learn long-term dependencies**.

---

## ⚠️ Vanishing Gradient Problem

One major issue with BPTT is the **vanishing gradient problem**.

During backpropagation:

* gradients may become extremely small
* early time steps receive very little learning signal

Example:

```text
Loss → t₁₀ → t₉ → t₈ → ... → t₁
```

Gradients shrink as they move backward.

This makes it difficult for RNNs to learn **long-term dependencies**.

Example difficulty:

```text
"The movie I watched yesterday evening was fantastic"
```

The model may forget earlier words like:

```text
movie
```

when predicting the sentiment.

---

## ⚠️ Exploding Gradient Problem

Another issue is the **exploding gradient problem**, where gradients become extremely large.

Effects:

* unstable training
* weight updates become too large
* model fails to converge

Common solution:

```text
Gradient Clipping
```

This limits the maximum gradient value during training.

---

## 🚀 Solutions to RNN Training Problems

To overcome these limitations, improved architectures were developed.

Examples include:

* **LSTM (Long Short-Term Memory)**
* **GRU (Gated Recurrent Unit)**

These architectures help RNNs remember **long-term information** more effectively.

---

## 🎯 Key Points

* RNNs are trained using **Backpropagation Through Time (BPTT)**.
* BPTT propagates gradients through **all time steps** in a sequence.
* Gradients update shared weights across the entire sequence.
* Basic RNNs suffer from **vanishing and exploding gradient problems**.

---

## 🧠 One-Line Summary

> Backpropagation Through Time (BPTT) is the training process used in RNNs where gradients are propagated backward through all time steps to update the network’s weights.
