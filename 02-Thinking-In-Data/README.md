# Thinking in Terms of Data

This project marks the transition from programming to data analysis.

Instead of writing logic for a single output, we process a dataset to extract meaning and decisions.

---

## Problem Statement

Given a raw customer feedback dataset containing inconsistent and messy entries, the goal is to:

- clean the dataset
- handle missing and incorrect values
- generate insights
- build a simple recommendation logic

---

## Project Files

- 📓 [Analysis Notebook](notebook/amazon_store_analysis.ipynb)
- 📄 [Raw Dataset](dataset/store_data.json)

---

## Dataset Description

The dataset contains customer reviews with fields:

- name
- rating
- feedback
- age

### Issues in Raw Data

- ratings written as words ("four", "two")
- ratings stored as strings
- missing age values
- duplicate users
- inconsistent formatting

---

## Workflow

### 1. Data Loading
Load JSON data into Python structure.

### 2. Data Cleaning
- normalize ratings
- handle missing values
- remove duplicates

### 3. Insights
- average rating
- percentage of poor ratings

### 4. Recommendation System
Simple rule-based recommendation:

- rating ≥ 4 → Apple
- rating < 4 → Samsung

---

## Learning Outcome

This project demonstrates how raw data is transformed into meaningful decisions.

Pipeline followed:

Raw Data → Cleaning → Insights → Recommendation

This forms the foundation of real machine learning workflows.
