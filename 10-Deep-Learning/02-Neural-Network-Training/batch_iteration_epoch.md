# 🔄 Batch vs Iteration vs Epoch

## 📌 Overview

When training neural networks, data is usually **too large to process all at once**.
Instead of feeding the entire dataset to the model in one step, we divide the data into **smaller groups called batches**.

During training, three important terms are used:

* **Batch**
* **Iteration**
* **Epoch**

Understanding these terms is important because they describe **how the model processes data during training**.

---

## 🧠 Intuition

Imagine studying for an exam with **100 practice questions**.

You decide to study **10 questions at a time**.

Your study process would look like this:

```
10 questions → study once → repeat until all 100 questions are completed
```

In this example:

* **Batch** → 10 questions
* **Iteration** → studying one batch
* **Epoch** → finishing all 100 questions once

The same idea applies when training neural networks.

---

## 📦 What is a Batch?

A **Batch** is a small subset of the training dataset used to train the model at one time.

Example:

```
Dataset size = 1000 samples
Batch size = 100
```

Each batch contains:

```
100 training samples
```

The dataset will be divided into:

```
1000 / 100 = 10 batches
```

Processing data in batches helps:

* reduce memory usage
* speed up training
* improve gradient estimation

---

## 🔁 What is an Iteration?

An **Iteration** refers to **one update of the model using one batch of data**.

Example:

```
Batch size = 100
Dataset = 1000 samples
```

Number of iterations needed to process the entire dataset:

```
1000 / 100 = 10 iterations
```

Each iteration includes:

```
Forward Propagation
Loss Calculation
Backpropagation
Weight Update
```

---

## 🔄 What is an Epoch?

An **Epoch** is one complete pass through the **entire training dataset**.

Example:

```
Dataset = 1000 samples
Batch size = 100
```

One epoch consists of:

```
10 iterations
```

Training usually requires **multiple epochs** so that the model can learn patterns gradually.

Example:

```
Epoch 1 → model learns basic patterns
Epoch 10 → model improves accuracy
Epoch 50 → model becomes well trained
```

---

## 📊 Example

Suppose we have:

```
Dataset size = 10,000 samples
Batch size = 100
Epochs = 20
```

Then:

Iterations per epoch:

```id="3mmcgj"
10,000 / 100 = 100 iterations
```

Total training iterations:

```id="jybbsn"
100 iterations × 20 epochs = 2000 iterations
```

---

## 🏗️ Training Flow

Training a neural network typically follows this process:

```
Epoch
   ↓
Batch
   ↓
Iteration
   ↓
Forward Propagation
Backpropagation
Weight Update
```

This process repeats until the model converges.

---

## ⚠️ Choosing the Batch Size

Batch size affects **training speed and stability**.

Small batch sizes:

* faster updates
* noisier gradients
* better generalization

Large batch sizes:

* more stable gradients
* requires more memory
* slower updates

Common batch sizes used in practice:

```
16
32
64
128
256
```

---

## ⚠️ Key Points to Remember

* **Batch** → small subset of training data
* **Iteration** → one update using one batch
* **Epoch** → one complete pass through the dataset
* Training usually runs for **multiple epochs**

---

## 🎓 Interview Insight

Common interview question:

**What is the difference between batch, iteration, and epoch?**

Answer:

* **Batch** → subset of training data
* **Iteration** → one model update using a batch
* **Epoch** → one complete pass through the entire dataset

Another question:

**Why do we use batches instead of the full dataset?**

Because training with batches reduces memory usage and improves computational efficiency.

---

## 🧠 One-Line Summary

> A batch is a subset of training data, an iteration is one model update using a batch, and an epoch is one complete pass through the entire dataset.
