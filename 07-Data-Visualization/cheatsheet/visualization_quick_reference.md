# Visualization Quick Reference

This file is a **fast revision cheatsheet** for Data Visualization using  
**Matplotlib & Seaborn**.

Use this when:
- you forget syntax
- revising before interviews
- quick recall during projects

---

# PART 1 — Matplotlib Basics

## Import Matplotlib

```python
import matplotlib.pyplot as plt
```

Common convention:

- `plt` → pyplot interface

---

## Figure vs Axes (Most Important Concept)

### Old (State-based) Style

```python
plt.plot(x, y)
plt.show()
```

Quick but less control.

### Modern (Object-Oriented) Style ✅

```python
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

- `fig` → entire figure (canvas)
- `ax` → plotting area

👉 Always prefer this for real projects

---

## Basic Plot

```python
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

---

## Labels & Title

```python
ax.set_title("My Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
```

---

## Legend

```python
ax.plot(x, y, label="Line 1")
ax.legend()
```

Used when multiple datasets exist.

---

## Grid

```python
ax.grid(True)
```

Improves readability.

---

## Saving Figures

```python
fig.savefig("plot.png", dpi=300, bbox_inches="tight")
```

Common formats:

- `.png`
- `.jpg`
- `.pdf`

---

## Minimal Complete Example

```python
fig, ax = plt.subplots()

ax.plot(x, y, label="Sample Line")
ax.set_title("Example Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
ax.grid(True)

plt.show()
```

---

## Mental Notes

`plt.plot()` → quick

`fig, ax = plt.subplots()` → professional

Always label axes

Always save plots for reports

---

# PART 2 — Line & Bar Charts

## Line Plot

Used for trends over time.

```python
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

With markers:

```python
ax.plot(x, y, marker="o")
```

With style:

```python
ax.plot(x, y, color="blue", linestyle="--", linewidth=2)
```

---

## Multiple Lines

Compare multiple datasets.

```python
ax.plot(x, y1, label="Dataset 1")
ax.plot(x, y2, label="Dataset 2")
ax.legend()
```

---

## Vertical Bar Chart

Used for category comparison.

```python
ax.bar(categories, values)
```

Colored bars:

```python
ax.bar(categories, values, color="skyblue")
```

---

## Horizontal Bar Chart

Better for long labels.

```python
ax.barh(categories, values)
```

Invert order (largest on top):

```python
ax.invert_yaxis()
```

---

## Grouped Bar Chart

Compare multiple groups.

```python
import numpy as np

x = np.arange(len(categories))
width = 0.35

ax.bar(x - width/2, values1, width, label="2022")
ax.bar(x + width/2, values2, width, label="2023")

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
```

---

## Add Labels on Bars

```python
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2,
            height,
            str(height),
            ha='center', va='bottom')
```

---

## Mental Notes

- Line → trends
- Bar → comparison
- Horizontal bar → long names
- Grouped bar → multi-category comparison

---

# PART 3 — Scatter Plots

Used to analyze relationship between two numerical variables.

---

## Basic Scatter

```python
fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show()
```

---

## Marker Size (Magnitude Encoding)

```python
sizes = [20, 50, 100, 200]

ax.scatter(x, y, s=sizes)
```

`s` → controls size of points

---

## Color Mapping

Single color:

```python
ax.scatter(x, y, color="red")
```

Multiple colors:

```python
colors = [1,2,3,4,5]

scatter = ax.scatter(x, y, c=colors, cmap="viridis")
plt.colorbar(scatter)
```

Used to represent third variable.

---

## Transparency (Density Handling)

```python
ax.scatter(x, y, alpha=0.5)
```

Useful when points overlap.

---

## Edge Colors

```python
ax.scatter(x, y, edgecolors="black")
```

Improves visibility.

---

## Annotation (Highlight Points)

```python
ax.scatter(x, y)

ax.annotate("Peak",
            xy=(x_peak, y_peak),
            xytext=(x_peak+1, y_peak+1),
            arrowprops=dict(arrowstyle="->"))
```

Used to explain important observations.

---

## Highlight Specific Point

```python
ax.scatter(x_peak, y_peak, color="red", s=120)
```

---

## Mental Notes

- Scatter → correlation
- size → magnitude
- color → category/value
- annotation → explain insight

---

# PART 4 — Distribution Plots (Matplotlib)

Used to understand spread, frequency, proportion, and contribution of data.

---

## Histogram

Shows frequency distribution of numerical values.

```python
fig, ax = plt.subplots()
ax.hist(data, bins=20)
plt.show()
```

Styled:

```python
ax.hist(data, bins=20, color="skyblue", edgecolor="black")
```

Add mean line:

```python
import numpy as np
mean = np.mean(data)
ax.axvline(mean, color="red", linestyle="--")
```

---

## Box Plot

Shows quartiles and outliers.

```python
ax.boxplot(data)
```

Horizontal:

```python
ax.boxplot(data, vert=False)
```

Multiple groups:

```python
ax.boxplot([data1, data2])
```

Show mean:

```python
ax.boxplot(data, showmeans=True)
```

---

## Pie Chart

Shows percentage share.

```python
ax.pie(values, labels=labels, autopct="%1.1f%%")
```

Explode slice:

```python
explode = [0.1, 0, 0, 0]
ax.pie(values, labels=labels, explode=explode, autopct="%1.1f%%")
```

---

## Stack Plot

Shows cumulative contribution over time.

```python
ax.stackplot(x, y1, y2, y3, labels=["A","B","C"])
ax.legend()
```

---

## Mental Notes

- Histogram → distribution
- Boxplot → outliers & spread
- Pie → proportions
- Stackplot → cumulative trends

---

# PART 5 — Subplots & Layout

Used to display multiple plots in a single figure.

---

## subplot() (Basic Method)

Syntax:

```python
plt.subplot(rows, cols, index)
```

Example:

```python
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.plot(x, y1)
plt.title("Plot 1")

plt.subplot(1,2,2)
plt.plot(x, y2)
plt.title("Plot 2")

plt.show()
```

## subplots() (Recommended Method ✅)

Creates figure and axes together.

```python
fig, ax = plt.subplots(1,2)

ax[0].plot(x, y1)
ax[0].set_title("Plot 1")

ax[1].plot(x, y2)
ax[1].set_title("Plot 2")

plt.show()
```

Grid layout:

```python
fig, axs = plt.subplots(2,2)

axs[0,0].plot(x, y)
axs[1,1].hist(data)
```

---

## tight_layout()

Fix overlapping labels automatically.

```python
plt.tight_layout()
```

Used after creating subplots.

---

## Mental Notes

- `subplot()` → quick & simple
- `subplots()` → professional & flexible
- always use `tight_layout()` for readability

---

# PART 6 — Seaborn Basics

Seaborn provides high-level statistical visualization built on top of Matplotlib.

Less code → More insight.

---

## Import Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

---

## Loading Built-in Dataset

```python
df = sns.load_dataset("tips")
df.head()
```

Common practice datasets:

- tips
- iris
- titanic
- flights

---

## Themes & Styling

Default style is already better than matplotlib.

Change theme:

```python
sns.set_theme(style="darkgrid")
```

Other styles:

```python
sns.set_theme(style="whitegrid")
sns.set_theme(style="ticks")
sns.set_theme(style="dark")
sns.set_theme(style="white")
```

---

## hue (Most Important Feature)

Separates data by category automatically.

```python
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
```

Seaborn groups and colors automatically.

---

## style Parameter

Different marker styles for categories.

```python
sns.scatterplot(data=df, x="total_bill", y="tip", style="time")
```

---

## size Parameter

Represents magnitude visually.

```python
sns.scatterplot(data=df, x="total_bill", y="tip", size="size")
```

---

## Combine hue + style + size

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    style="time",
    size="size"
)
```

---

## Mental Notes

- Seaborn understands DataFrame directly
- hue = category
- size = magnitude
- style = marker difference

---

# PART 7 — Seaborn Relational & Categorical

Used for relationship analysis and group comparison.

---

## scatterplot()

Shows relationship between two numerical variables.

```python
sns.scatterplot(data=df, x="total_bill", y="tip")
```

With category separation:

```python
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
```

---

## lineplot()

Shows trend over time or ordered variable.

```python
sns.lineplot(data=df, x="size", y="total_bill")
```

Grouped line:

```python
sns.lineplot(data=df, x="size", y="total_bill", hue="sex")
```

---

## barplot()

Shows average value per category.

```python
sns.barplot(data=df, x="day", y="total_bill")
```

Grouped:

```python
sns.barplot(data=df, x="day", y="total_bill", hue="sex")
```

---

## countplot()

Counts frequency of categories.

```python
sns.countplot(data=df, x="day")
```

---

## boxplot()

Shows distribution + outliers per category.

```python
sns.boxplot(data=df, x="day", y="total_bill")
```

Grouped:

```python
sns.boxplot(data=df, x="day", y="total_bill", hue="sex")
```

---

## violinplot()

Shows density + distribution shape.

```python
sns.violinplot(data=df, x="day", y="total_bill")
```

---

## Mental Notes

- scatter → relationship
- line → trends
- bar → averages
- count → frequency
- box → spread & outliers
- violin → distribution shape

---

# PART 8 — Seaborn Distributions

Used to understand how data is distributed.

---

## histplot()

Shows frequency distribution.

```python
sns.histplot(data=df, x="total_bill")
```

With bins:

```python
sns.histplot(data=df, x="total_bill", bins=20)
```

With KDE:

```python
sns.histplot(data=df, x="total_bill", kde=True)
```

---

## kdeplot()

Smooth probability density curve.

```python
sns.kdeplot(data=df, x="total_bill")
```

Compare categories:

```python
sns.kdeplot(data=df, x="total_bill", hue="sex", fill=True)
```

---

## jointplot()

Relationship + distributions together.

```python
sns.jointplot(data=df, x="total_bill", y="tip")
```

Types:

```python
sns.jointplot(data=df, x="total_bill", y="tip", kind="kde")
sns.jointplot(data=df, x="total_bill", y="tip", kind="hex")
```

---

## pairplot()

Most powerful EDA plot.

Shows relationships between all numerical features.

```python
sns.pairplot(df)
```

Grouped:

```python
sns.pairplot(df, hue="sex")
```

---

## Mental Notes

- histplot → frequency
- kdeplot → density
- jointplot → 2-variable relationship
- pairplot → full dataset overview

---

# PART 9 — Heatmaps & Correlation

Used for feature relationships and feature selection before ML.

---

## Correlation Matrix

Calculates relationship between numerical columns.

```python
corr_matrix = df.corr(numeric_only=True)
corr_matrix
```

Range:

- +1 → strong positive relation
- 0 → no relation
- -1 → strong negative relation

---

## Heatmap

Visual representation of correlation matrix.

```python
sns.heatmap(corr_matrix)
```

---

## Annotated Heatmap (Recommended)

Shows values inside cells.

```python
sns.heatmap(corr_matrix, annot=True)
```

Better styling:

```python
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)
```

---

## Mask Upper Triangle (Cleaner View)

```python
import numpy as np

mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, cmap="coolwarm")
```

---

## Mental Notes

- Always check correlation before ML
- Remove highly correlated features
- Helps feature selection

---

# PART 10 — Visualization Best Practices

Good visualization = Clear communication  
Bad visualization = Misleading analysis

---

## When to Use Which Plot

| Goal | Recommended Plot |
|----|----|
Trend over time | Line plot
Compare categories | Bar chart
Relationship between variables | Scatter plot
Distribution of values | Histogram
Spread & outliers | Box plot
Density shape | Violin plot / KDE
Feature relationships | Pairplot
Correlation check | Heatmap
Percentage share | Pie chart (rarely)

---

## Common Mistakes ❌

### 1. Too Many Colors
Bad:
```python
plt.plot(x, y, color="red")
plt.plot(x, z, color="green")
plt.plot(x, w, color="yellow")
```
Hard to read.

### 2. Missing Labels

Never do:

```python
plt.plot(x, y)
```

Always do:

```python
plt.xlabel("Time")
plt.ylabel("Sales")
plt.title("Sales Over Time")
```

### 3. Misleading Axis Scale

Avoid cutting axis to exaggerate change.

Bad:

```python
y-axis starts at 95 instead of 0
```

### 4. Overplotting

Too many points → unreadable.

Solution:

```python
alpha=0.4
```

### 5. Using Wrong Chart Type

Pie chart for 20 categories ❌
Use bar chart instead ✔️

---

## Rules for Readability

### Always Follow

- Add title
- Label axes
- Use legend
- Use grid when needed
- Use consistent colors
- Keep background simple

---

## Good Color Choices

Prefer:

- blue / orange / green
- colorblind-friendly palettes

Seaborn palette:

```python
sns.set_palette("deep")
```

---

## Keep It Simple

Golden rule:

- A plot should be understandable in 5 seconds.

---

## Final Mental Model

Visualization Purpose:

1. Understand data (EDA)
2. Detect problems
3. Explain results

Not decoration — communication.