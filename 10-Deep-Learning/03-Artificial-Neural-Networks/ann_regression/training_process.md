# 🧠 ANN Training Process

## 📌 Overview

After loading and preparing the dataset, the next step is **training the Artificial Neural Network (ANN)**.

Training is the process where the neural network **learns patterns from data** by adjusting its **weights and biases** to reduce prediction error.

The training loop repeatedly performs the following steps:

```text
Forward Propagation → Compute Loss → Backpropagation → Update Weights
```

This cycle runs multiple times until the model learns the relationship between **input features and the target variable**.

---

## ⚙️ Model Architecture

In this example, we use a simple **Feedforward Neural Network**.

The network consists of:

* **Input Layer** → receives feature values
* **Hidden Layers** → learn complex relationships
* **Output Layer** → produces the predicted value

Architecture used in the notebook:

```text
Input (4 features)
      ↓
Hidden Layer (16 neurons)
      ↓
Hidden Layer (8 neurons)
      ↓
Output Layer (1 neuron)
```

Since this is a **regression problem**, the output layer contains **only one neuron**.

---

## 🔄 Forward Propagation

Forward propagation is the process where **input data flows through the neural network to produce predictions**.

Each neuron performs a weighted sum:

```
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```

Then an activation function is applied.

In this model we use **ReLU activation** for hidden layers.

The forward pass in the notebook is implemented inside the model's `forward()` function.

Example:

```python
def forward(self, x):

    x = self.relu(self.layer1(x))
    x = self.relu(self.layer2(x))
    x = self.output(x)

    return x
```

The output of this step is the **predicted value**.

---

## 📉 Loss Calculation

After obtaining predictions, we measure how far they are from the actual values.

For regression problems, we commonly use:

```
Mean Squared Error (MSE)
```

The loss function computes the difference between:

```
Predicted Output vs Actual Output
```

In the notebook:

```python
criterion = nn.MSELoss()
```

The training goal is to **minimize this loss**.

---

## 🔙 Backpropagation

Backpropagation calculates the **gradients of the loss with respect to model parameters**.

Gradients tell us:

```
How much each weight contributed to the prediction error
```

The gradients are computed using **automatic differentiation in PyTorch**.

Example from the notebook:

```python
loss.backward()
```

This step prepares the model for parameter updates.

---

## ⚡ Weight Updates (Optimization)

After computing gradients, the optimizer updates the weights.

In the notebook we use the **Adam optimizer**.

Example:

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

The optimizer updates weights using gradient descent-based rules to **reduce the loss**.

Parameter update step:

```python
optimizer.step()
```

Before computing new gradients, previous gradients are cleared:

```python
optimizer.zero_grad()
```

---

## 🔁 Training Loop

The entire training process runs inside a loop across multiple **epochs**.

Example structure used in the notebook:

```python
for epoch in range(epochs):

    predictions = model(X_train)

    loss = criterion(predictions, y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
```

Each epoch allows the neural network to **improve its predictions gradually**.

---

## 📈 Monitoring Training Progress

During training, the loss value is tracked to observe how the model improves.

Example output from the notebook:

```
Epoch [10/100], Loss: 206461
Epoch [50/100], Loss: 206080
Epoch [100/100], Loss: 205097
```

A decreasing loss indicates that the model is **learning from the data**.

The training loss curve plotted in the notebook helps visualize this improvement.

---

## ⚠️ Important Points

* Neural networks learn by **minimizing the loss function**.
* Backpropagation computes gradients automatically in PyTorch.
* Optimizers update the weights using gradient information.
* Training requires multiple **epochs** to learn patterns effectively.

---

## 🔗 Related Implementation

The full implementation of the training process can be found in:

📄 `ann_regression.ipynb`

This notebook demonstrates how the ANN is defined, trained, and evaluated using PyTorch.

---

## 🧠 One-Line Summary

> The ANN training process repeatedly performs forward propagation, loss calculation, backpropagation, and weight updates to minimize prediction error and improve model performance.
