# 🏗️ Building the ANN Model

## 📌 Overview

In this step we design the **Artificial Neural Network (ANN)** used for the classification task.

A neural network is composed of multiple layers that transform input features into predictions.
Each layer learns patterns from the data through **weighted connections and activation functions**.

For this classification problem, we use a **Feedforward Neural Network (FNN)** implemented using **PyTorch**.

---

## 🧠 Neural Network Architecture

The neural network used in the notebook consists of:

* **Input Layer**
* **Hidden Layers**
* **Output Layer**

Architecture used:

```text
Input Layer (number of features)
        ↓
Hidden Layer (64 neurons)
        ↓
Hidden Layer (32 neurons)
        ↓
Hidden Layer (16 neurons)
        ↓
Output Layer (number of classes)
```

Explanation:

* The **input layer** receives feature values from the dataset.
* **Hidden layers** learn complex relationships between features.
* The **output layer** predicts the class of the input sample.

---

## ⚙️ Activation Function

The hidden layers use the **ReLU (Rectified Linear Unit)** activation function.

ReLU formula:

```
ReLU(x) = max(0, x)
```

Why ReLU is used:

* computationally efficient
* helps reduce vanishing gradient problems
* commonly used in deep learning models

ReLU introduces **non-linearity**, allowing the network to learn complex patterns.

---

## 🧩 Output Layer for Classification

The final layer outputs **raw class scores (logits)**.

These logits represent how strongly the model believes the input belongs to each class.

Example output:

```text
[2.1, 0.4, -1.2, 3.0, 0.8]
```

During training, these values are passed to the **CrossEntropyLoss** function, which internally applies **Softmax**.

Because of this, we **do not apply Softmax manually in the model**.

---

## ⚙️ Model Implementation in PyTorch

The neural network is implemented using the `nn.Module` class.

Example implementation:

```python
class ANNClassifier(nn.Module):

    def __init__(self, input_size, num_classes):
        super(ANNClassifier, self).__init__()

        self.layer1 = nn.Linear(input_size, 64)
        self.layer2 = nn.Linear(64, 32)
        self.layer3 = nn.Linear(32, 16)
        self.output = nn.Linear(16, num_classes)

        self.relu = nn.ReLU()

    def forward(self, x):

        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.relu(self.layer3(x))
        x = self.output(x)

        return x
```

This class defines:

* the network layers
* the activation functions
* the forward pass of the model

---

## 🔄 Forward Pass

The **forward pass** defines how input data moves through the neural network.

Steps in the forward pass:

1. Input features enter the network
2. Data passes through hidden layers
3. Activation functions introduce non-linearity
4. Output layer produces class scores

This process produces the **predicted class probabilities** used during training.

---

## ⚠️ Important Points

* The number of neurons controls the **model capacity**.
* Too few neurons may lead to **underfitting**.
* Too many neurons may cause **overfitting**.
* Hidden layers use **ReLU activation**.
* The output layer produces **logits for classification**.

---

## 🎯 Key Takeaway

> Building an ANN involves defining the network architecture, selecting activation functions, and implementing the forward pass so that the model can transform input features into class predictions.
