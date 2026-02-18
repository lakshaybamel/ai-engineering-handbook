# Matplotlib

Matplotlib is the foundational plotting library in Python.

It provides complete control over figures, axes, styling, and layout.
Most higher-level libraries (like Seaborn) are built on top of Matplotlib.

---

# Why Matplotlib Matters

Matplotlib is used for:

• Exploratory Data Analysis (EDA)  
• Reporting & dashboards  
• Publication-quality figures  
• Custom visualizations  

It gives low-level control over every visual element.

---

# Plotting Approaches in Matplotlib

There are two main styles:

---

## 1️⃣ Pyplot (Simple Way)

```python
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.show()
```

Good for quick analysis.

---

## 2️⃣ Object-Oriented Style (Modern Way)

```python
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

Preferred for:

- dashboards
- complex figures
- multiple subplots

---

# Matplotlib — Topics Covered in This Module


## 🔹 Basics

📂 [Plotting Basics](basics/01_plotting_basics.ipynb)  
📂 [Format Strings](basics/02_format_strings.ipynb)  
📂 [Styling & Saving](basics/03_styling_saving.ipynb)  

**Covered:**
- creating plots
- adding labels & titles
- format strings (color, marker, linestyle)
- grid, ticks, limits
- saving figures

---

## 🔹 Line Plots

📂 [Single Line Plot](line_plots/01_single_line.ipynb)  
📂 [Multiple Lines](line_plots/02_multiple_lines.ipynb)  

**Used for:**
- trends over time
- growth analysis
- performance comparison

---

## 🔹 Bar Charts

📂 [Vertical Bar](bar_charts/01_vertical_bar.ipynb)  
📂 [Horizontal Bar](bar_charts/02_horizontal_bar.ipynb)  
📂 [Grouped Bars & Labels](bar_charts/03_multiple_bar_labels.ipynb)  

**Used for:**
- category comparison
- multi-year sales comparison
- performance metrics

---

## 🔹 Scatter Plots

📂 [Basic Scatter](scatter_plots/01_basic_scatter.ipynb)  
📂 [Customization](scatter_plots/02_customization.ipynb)  
📂 [Annotations & Multi Scatter](scatter_plots/03_annotations_multi.ipynb)  

**Used for:**
- correlation analysis
- outlier detection
- relationship between variables

---

## 🔹 Distribution Plots

📂 [Histograms](distributions/01_histograms.ipynb)  
📂 [Box Plot](distributions/02_boxplot.ipynb)  
📂 [Pie Chart](distributions/03_pie_chart.ipynb)  

**Used for:**
- distribution analysis
- spread & quartiles
- percentage breakdown

---

## 🔹 Advanced Plots

📂 [Stack Plot](advanced/01_stackplot.ipynb)  
📂 [Subplots](advanced/02_subplots.ipynb)  
📂 [Modern Matplotlib](advanced/03_modern_matplotlib.ipynb)  

**Covered:**
- cumulative trends
- dashboards
- object-oriented plotting
- professional figure control

---

## 🔹 Practice Project

📂 [Weekly Temperature Analysis](practice/weekly_temperature_task.ipynb)  

Mini EDA project demonstrating:
- trend analysis
- distribution
- comparison
- annotations

---

# Common Plot Types Summary

| Plot Type | Purpose |
|--------|------|
| Line Plot | Trends over time |
| Bar Chart | Category comparison |
| Scatter Plot | Relationship analysis |
| Histogram | Distribution analysis |
| Box Plot | Spread & Outlier detection |
| Pie Chart | Percentage share |
| Stack Plot | Cumulative contribution |
| Subplots | Multi-figure dashboards |

---

# Key Concepts Learned

- figure vs axes
- format strings
- legends & labels
- grid & styling
- saving high-resolution images
- object-oriented plotting

---

# Mental Model

**Matplotlib is:**

Low-level → maximum control → professional visualization

Always use Object-Oriented style for serious projects.

---

# Position in Data Science Workflow

Data Collection → Cleaning → Visualization (Matplotlib) → Feature Engineering → Modeling

Visualization helps:
- detect anomalies
- understand distributions
- validate preprocessing
- present results clearly