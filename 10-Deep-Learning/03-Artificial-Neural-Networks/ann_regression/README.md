# 🧠 Artificial Neural Network (ANN) for Regression

This section demonstrates how to build and train an **Artificial Neural Network (ANN)** to solve a **regression problem** using **PyTorch**.

The goal of this example is to predict the **power output of a power plant** based on environmental conditions such as temperature, pressure, humidity, and exhaust vacuum.

This module walks through the **complete workflow of training a neural network for regression**, including:

* dataset preparation
* model architecture
* training process
* model evaluation

---

# 📂 Files in This Section

### 📓 Implementation Notebook

📄 [ann_regression.ipynb](ann_regression.ipynb)

The main notebook containing the **full implementation of the ANN regression model**.

The notebook includes:

* dataset loading
* preprocessing and scaling
* neural network architecture
* training loop
* loss tracking
* model evaluation

---

### 📊 Dataset Explanation

📄 [dataset_loading.md](dataset_loading.md)

Explains the dataset used for training the neural network.

Topics covered:

* dataset structure
* feature descriptions
* separating input features and target variable
* train-test split
* feature scaling

---

### ⚙️ Training Process

📄 [training_process.md](training_process.md)

Explains how the neural network is trained.

Topics covered:

* model architecture
* forward propagation
* loss calculation
* backpropagation
* weight updates using optimizers
* training loop and epochs

---

### 📈 Model Evaluation

📄 [evaluation.md](evaluation.md)

Describes how the trained model is evaluated.

Topics covered:

* regression evaluation metrics
* Root Mean Squared Error (RMSE)
* interpreting prediction error
* visualizing model predictions

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ how neural networks solve **regression problems**  
✔ how to build an **ANN using PyTorch**  
✔ how training works using **forward and backward propagation**  
✔ how to evaluate regression models using **RMSE**  

This example serves as a **foundation for applying neural networks to continuous prediction tasks**.

---

# 🔗 Next Section

After understanding ANN for regression, the next step is to explore **ANN for classification**.

➡️ [ann_classification](../ann_classification/README.md)

In that section we will build a neural network that predicts **categorical outputs instead of continuous values**.

---

# 🧠 Key Takeaway

> Artificial Neural Networks can learn complex relationships between input variables and continuous outputs, making them powerful tools for solving regression problems.
