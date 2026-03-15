# 🧠 LSTM (Long Short-Term Memory) Network

## 📌 Overview

**Long Short-Term Memory (LSTM)** is a special type of **Recurrent Neural Network (RNN)** designed to overcome the limitations of traditional RNNs.

Standard RNNs struggle with learning **long-term dependencies** because of the **vanishing gradient problem**.

LSTM networks solve this issue by introducing a **memory cell and gating mechanisms** that allow the network to:

* remember important information
* forget irrelevant information
* control the flow of information over time

Because of this ability, LSTMs are widely used for tasks involving **long sequences**.

---

## 🧠 Intuition

Consider the sentence:

```text
"The movie I watched yesterday was fantastic"
```

To correctly predict the sentiment, the model must remember earlier words like:

```text
movie
fantastic
```

Traditional RNNs may forget earlier words when processing long sequences.

LSTMs introduce a **memory cell** that allows the network to **retain important information for long periods**.

Example idea:

```text
Important information → stored in memory
Irrelevant information → forgotten
```

This selective memory helps LSTMs learn **long-term relationships in sequences**.

---

## 🧩 Structure of an LSTM Cell

An LSTM cell is more complex than a standard RNN neuron.

It contains:

* **Cell State (memory)**
* **Hidden State**
* **Three gates**

The three gates are:

1️⃣ **Forget Gate**
2️⃣ **Input Gate**
3️⃣ **Output Gate**

These gates control how information flows through the network.

---

## 🔄 Cell State (Memory)

The **cell state** acts like a **long-term memory** that carries information across time steps.

Flow:

```text
Previous Cell State → Updated Cell State → Next Cell State
```

This memory allows LSTM networks to **preserve information over long sequences**.

---

## 🚪 Forget Gate

The **forget gate** decides which information should be removed from the cell state.

Example:

```text
Forget irrelevant words
```

Example sentence:

```text
"The movie I watched yesterday was fantastic"
```

The model may forget words like:

```text
yesterday
```

because they may not contribute to sentiment.

Forget gate equation:

```text
fₜ = σ(Wf · [hₜ₋₁, xₜ] + bf)
```

Where:

* **σ** → sigmoid activation
* **xₜ** → current input
* **hₜ₋₁** → previous hidden state

The output is a value between **0 and 1**, indicating how much information to keep.

---

## ➕ Input Gate

The **input gate** decides which new information should be added to the memory.

Two steps occur:

1️⃣ Determine which values to update
2️⃣ Create candidate memory values

Input gate equation:

```text
iₜ = σ(Wi · [hₜ₋₁, xₜ] + bi)
```

Candidate memory:

```text
C̃ₜ = tanh(Wc · [hₜ₋₁, xₜ] + bc)
```

The memory is then updated using:

```text
Cₜ = fₜ * Cₜ₋₁ + iₜ * C̃ₜ
```

This step allows the network to **add useful new information to memory**.

---

## 📤 Output Gate

The **output gate** determines which part of the memory should be used to generate the output.

Output gate equation:

```text
oₜ = σ(Wo · [hₜ₋₁, xₜ] + bo)
```

Hidden state calculation:

```text
hₜ = oₜ * tanh(Cₜ)
```

This hidden state becomes the **output of the LSTM cell** and is passed to the next time step.

---

## ⚙️ LSTM Flow Summary

At each time step, the LSTM performs:

```text
1. Decide what to forget
2. Decide what to store
3. Update memory cell
4. Produce output
```

This gating mechanism allows the network to **retain useful information while discarding irrelevant details**.

---

## 📊 RNN vs LSTM

| Feature                       | RNN     | LSTM             |
| ----------------------------- | ------- | ---------------- |
| Memory capability             | Limited | Long-term memory |
| Vanishing gradient problem    | Severe  | Reduced          |
| Architecture complexity       | Simple  | More complex     |
| Performance on long sequences | Poor    | Much better      |

Because of this, LSTMs are often preferred for **long sequence tasks**.

---

## 🚀 Applications of LSTM

LSTMs are widely used in many sequence modeling problems.

Examples include:

* **sentiment analysis**
* machine translation
* speech recognition
* text generation
* time series forecasting

Example NLP task:

```text
Input: "This movie was amazing"
Output: Positive Sentiment
```

---

## ⚠️ Important Points

* LSTM is an improved version of **Recurrent Neural Networks**.
* It uses **memory cells and gates** to control information flow.
* LSTMs solve the **vanishing gradient problem** present in basic RNNs.
* They are effective for **long sequence modeling tasks**.

---

## 🧠 One-Line Summary

> LSTM networks extend traditional RNNs by introducing memory cells and gating mechanisms that allow the model to capture long-term dependencies in sequential data.
