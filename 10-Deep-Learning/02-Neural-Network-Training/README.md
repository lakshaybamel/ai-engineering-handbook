# 🧠 Neural Network Training

Training is the process through which a **neural network learns patterns from data**.

During training, the model makes predictions, measures the error using a **loss function**, and updates its parameters to reduce that error.

The basic learning cycle of a neural network is:

```text
Forward Propagation → Compute Loss → Backpropagation → Update Weights
```

This process repeats multiple times until the model learns meaningful patterns from the data.

---

# 📚 Topics Covered

## 1️⃣ Forward Propagation

📄 [forward_propagation.md](forward_propagation.md)

Forward propagation is the process where **input data passes through the neural network to generate predictions**.

Topics covered:

* how data flows through layers
* weighted sum computation
* activation functions
* producing model predictions

---

## 2️⃣ Backpropagation

📄 [backward_propagation.md](backward_propagation.md)

Backpropagation is the process of **propagating errors backward through the network to compute gradients**.

Topics covered:

* gradient computation
* error propagation through layers
* role of gradients in learning

---

## 3️⃣ Chain Rule in Neural Networks

📄 [chain_rule_nn.md](chain_rule_nn.md)

The **chain rule from calculus** is used during backpropagation to compute gradients across multiple layers.

Topics covered:

* derivatives in neural networks
* gradient calculation through multiple layers
* role of chain rule in backpropagation

---

## 4️⃣ Weight and Bias Updates

📄 [weight_bias_update.md](weight_bias_update.md)

Once gradients are computed, the model updates its **weights and biases** to minimize the loss.

Topics covered:

* parameter update rule
* role of learning rate
* how models gradually improve predictions

---

## 5️⃣ Batch, Iteration, and Epoch

📄 [batch_iteration_epoch.md](batch_iteration_epoch.md)

These terms describe **how training data is processed during model training**.

Topics covered:

* what a batch is
* difference between iteration and epoch
* how datasets are processed during training

---

## 6️⃣ Vanishing Gradient Problem

📄 [vanishing_gradient_problem.md](vanishing_gradient_problem.md)

Deep neural networks can face training difficulties due to **vanishing gradients**.

Topics covered:

* why gradients become very small
* how this affects early layers
* common techniques used to reduce this problem

---

# ⚡ Activation Functions

📁 [activation_functions/README.md](activation_functions/README.md)

Activation functions introduce **non-linearity** into neural networks, enabling them to learn complex patterns.

Topics include:

* overview of activation functions
* ReLU and its variants

---

# 📉 Loss Functions

📁 [loss_functions/README.md](loss_functions/README.md)

Loss functions measure the **difference between predicted values and actual values**.

Topics include:

* regression loss functions
* classification loss functions

---

# ⚙️ Optimization Techniques

📁 [optimization/README.md](optimization/README.md)

Optimization algorithms update model parameters to **minimize the loss function**.

Topics include:

* gradient descent
* optimizers
* modern variants of gradient descent

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ how neural networks **make predictions**  
✔ how models **calculate and propagate errors**  
✔ how parameters are **updated during training**  
✔ how activation functions, loss functions, and optimizers work together  

These concepts form the **core mechanics of deep learning training**.

---

# 🔗 Next Section

After understanding neural network training, we move to implementing actual neural networks.

Next module:

📁 [**Artificial Neural Networks (ANN)**](../03-Artificial-Neural-Networks/README.md)

In that section we will build neural networks for:

* regression problems
* classification problems

---

# 🧠 Key Takeaway

> Neural network training combines forward propagation, backpropagation, loss functions, and optimization techniques to gradually improve model predictions.
