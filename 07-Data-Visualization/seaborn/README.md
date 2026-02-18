# Seaborn

Seaborn is a high-level statistical visualization library built on top of Matplotlib.

It provides:
- better default styling
- simpler syntax
- statistical plots
- dataset-aware plotting

Seaborn is preferred for **EDA (Exploratory Data Analysis)**.

---

# Why Seaborn

Matplotlib → control  
Seaborn → understanding

Seaborn automatically handles:
- grouping
- aggregation
- confidence intervals
- distributions

Less code, more insight.

---

# Topics Covered

---

## 🔹 Basic Plots

📂 [Basic Plots](01_basic_plots.ipynb)

Covered:
- loading datasets
- scatterplot
- lineplot
- themes & styles

---

## 🔹 Relational Plots

📂 [Relational Plots](02_relational_plots.ipynb)

Used for:
- variable relationships
- trends
- multi-variable comparison

Key parameters:
- hue
- size
- style

---

## 🔹 Categorical Plots

📂 [Categorical Plots](03_categorical_plots.ipynb)

Used for:
- group comparison
- feature analysis

Includes:
- barplot
- countplot
- boxplot
- violinplot
- stripplot
- catplot

---

## 🔹 Distribution Plots

📂 [Distribution Plots](04_distribution_plots.ipynb)

Used for:
- normality check
- skewness
- density estimation

Includes:
- histplot
- kdeplot
- jointplot
- pairplot

---

## 🔹 Heatmaps

📂 [Heatmaps](05_heatmaps.ipynb)

Most important for ML:
- correlation analysis
- feature selection

---

# Common Seaborn Plot Types

| Plot | Purpose |
|----|----|
scatterplot | relationship between variables |
lineplot | trends |
barplot | category averages |
boxplot | distribution spread |
violinplot | density + distribution |
histplot | distribution |
pairplot | multi-variable relationship |
heatmap | correlation matrix |

---

# Mental Model

Seaborn answers:

"What does the data mean?"

Matplotlib answers:

"How should the graph look?"

---

# Position in Workflow

Data Collection → Cleaning → Visualization → **Seaborn EDA** → Feature Engineering → Modeling

Seaborn is mainly used before machine learning to understand the dataset.
