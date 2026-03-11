# 📊 Dataset Loading

## 📌 Overview

Before training a neural network, the first step is to **load and understand the dataset**.

In this example, we use the **Combined Cycle Power Plant Dataset** to train an **Artificial Neural Network (ANN) for regression**.

The dataset contains environmental variables that affect the **energy output of a power plant**.

Our goal is to train the neural network to **predict the power output based on these input features**.

---

## 📂 Dataset Used

File:

```
powerplant_dataset.csv
```

Location in repository:

```
10-Deep-Learning/datasets/powerplant_dataset.csv
```

This dataset is commonly used for **regression tasks in machine learning**.

---

## 🧾 Dataset Features

The dataset contains the following columns:

| Feature | Description                     |
| ------- | ------------------------------- |
| **AT**  | Ambient Temperature             |
| **V**   | Exhaust Vacuum                  |
| **AP**  | Ambient Pressure                |
| **RH**  | Relative Humidity               |
| **PE**  | Energy Output (Target Variable) |

Input variables:

```
AT, V, AP, RH
```

Target variable:

```
PE
```

The neural network learns a mapping:

```
Environmental Features → Power Output
```

---

## ⚙️ Loading the Dataset

We load the dataset using **Pandas**, a popular Python library for data handling.

Example:

```python
import pandas as pd

df = pd.read_csv("../../datasets/powerplant_dataset.csv")
```

After loading the dataset, we usually inspect the first few rows:

```python
df.head()
```

This helps verify that the dataset has been loaded correctly.

---

## 🔍 Understanding the Data

Once the dataset is loaded, it is good practice to inspect the data.

Example checks:

```python
df.shape
df.info()
df.describe()
```

These commands help us understand:

* number of rows and columns
* data types
* statistical properties of features

Understanding the dataset is important before training the model.

---

## 🧩 Separating Features and Target

Machine learning models require:

* **input features (X)**
* **target variable (y)**

Example:

```python
X = df.drop("PE", axis=1)
y = df["PE"]
```

Where:

```
X → input variables
y → output variable
```

The model will learn to predict **y from X**.

---

## 🔀 Train-Test Split

To evaluate model performance properly, the dataset is split into:

```
Training Data
Testing Data
```

Training data is used to **train the neural network**, while testing data is used to **evaluate model performance on unseen data**.

Example:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

Typical split:

```
80% → training data
20% → testing data
```

---

## 📏 Feature Scaling

Neural networks perform better when input features are **scaled or normalized**.

Why scaling is important:

* prevents large feature values from dominating
* improves gradient descent convergence
* stabilizes training

Example using **StandardScaler**:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Scaling ensures that all features have a **similar range**.

---

## 🎯 Key Points

* Dataset loading is the **first step in the ML pipeline**.
* Features and target variables must be separated.
* Data should be split into **training and testing sets**.
* Feature scaling improves neural network training.

Proper data preparation helps ensure **stable and efficient model training**.

---

## 🧠 One-Line Summary

> Dataset loading and preprocessing prepare the data so that neural networks can learn patterns effectively during training.
