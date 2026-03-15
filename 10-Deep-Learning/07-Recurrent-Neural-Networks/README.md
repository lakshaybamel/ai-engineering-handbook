# 🔁 Recurrent Neural Networks (RNN)

## 📌 Overview

Recurrent Neural Networks (RNNs) are a class of neural networks designed to process **sequential data**.

Unlike traditional feedforward neural networks, which assume that inputs are independent, RNNs maintain a **memory of previous inputs**. This allows them to capture **temporal and contextual relationships** within sequences.

RNNs are widely used in tasks involving **ordered data**, such as:

* Natural Language Processing (NLP)
* speech recognition
* machine translation
* time series forecasting

In this section, we explore how RNNs process sequences and how advanced architectures like **LSTM** improve their performance.

---

# 📂 Topics Covered

### 🔁 RNN Architecture

📄 [rnn_architecture.md](rnn_architecture.md)

Introduces the basic architecture of Recurrent Neural Networks and explains how they process sequential data.

Topics include:

* sequential data processing
* hidden state (memory)
* unrolled RNN structure
* mathematical formulation of RNNs

---

### 🧩 Types of RNN Architectures

📄 [types_of_rnn.md](types_of_rnn.md)

Explains different input-output structures used in RNN models.

Topics include:

* one-to-one architecture
* one-to-many architecture
* many-to-one architecture
* many-to-many architecture
* encoder–decoder models

---

### 🔙 Backpropagation in RNN

📄 [backpropagation_in_rnn.md](backpropagation_in_rnn.md)

Describes how RNNs are trained using **Backpropagation Through Time (BPTT)**.

Topics include:

* forward pass in RNN
* unrolled RNN training
* gradient flow across time steps
* vanishing gradient problem
* exploding gradient problem

---

### 🧠 LSTM Network

📄 [lstm_network.md](lstm_network.md)

Introduces **Long Short-Term Memory (LSTM)** networks, an improved RNN architecture designed to handle long-term dependencies.

Topics include:

* memory cells
* forget gate
* input gate
* output gate
* advantages over traditional RNNs

---

### 🧪 RNN Sentiment Analysis Implementation

📄 [rnn_sentiment_analysis.ipynb](rnn_sentiment_analysis.ipynb)

A practical implementation of **sentiment analysis using a Recurrent Neural Network**.

The notebook demonstrates:

* text preprocessing with **Regex**
* removing **stopwords using NLTK**
* **stemming and TF-IDF vectorization**
* creating **PyTorch DataLoaders**
* building an **RNN model**
* training and evaluating the model

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ how RNNs process sequential data  
✔ how hidden states allow networks to remember past information  
✔ how **Backpropagation Through Time (BPTT)** trains RNNs  
✔ how **LSTM networks solve the vanishing gradient problem**  
✔ how to implement an **RNN for sentiment analysis using PyTorch**  

---

# 🧠 Key Takeaway

> Recurrent Neural Networks process sequential data by maintaining a hidden state that carries contextual information across time steps, allowing models to learn patterns in sequences such as text and time series data.
