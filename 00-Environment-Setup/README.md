# Development Environment Setup (Data Workflow)

This section documents the environment used for data analysis and machine learning experiments.

After learning Python programming in VS Code, the workflow shifts to interactive computing using Jupyter notebooks.

---

## Why Not VS Code for Data?

**Normal programming**
- write full program
- run once
- get output

**Data analysis**
- test small steps
- inspect data
- modify logic repeatedly
- visualize results

Jupyter allows executing code step-by-step.

---

## Anaconda

Anaconda is used because it provides:
- Python
- package manager (conda)
- isolated environments
- data science libraries

This avoids dependency conflicts between projects.

---

## Conda Environment

Environments allow separate setups for different projects.

Typical workflow:

conda create -n ai-env python=3.11<br>
conda activate ai-env


All data libraries are installed inside this environment.

---

## Jupyter Notebook & Jupyter Lab

Jupyter provides interactive coding.

File type: `.ipynb`

Features:
- run code cell-by-cell
- view outputs instantly
- inspect datasets
- ideal for experimentation

Notebook → simple interface  
Lab → full IDE-style interface

---

## Workflow Transition

**Programming Phase**<br>
.py files → VS Code → program execution


**Data Phase**<br   >
.ipynb notebooks → Jupyter → data exploration


This marks the shift from software development to data thinking.