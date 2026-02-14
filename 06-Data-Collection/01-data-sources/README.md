# Data Sources

Before analysis or machine learning, the first step is obtaining data.

Models do not create value — data does.

---

## Population vs Sample

In real-world scenarios, collecting all data (population) is often impossible.

Instead, we work with a subset called a sample.

Example:
- Population → all customers of an e-commerce platform
- Sample → customers active in last 6 months

Machine learning models learn patterns from samples and generalize to population.

---

## Common Sources of Data

### 1. Databases
Structured business data stored in relational databases.

Examples:
- orders
- users
- transactions

Accessed using SQL.

---

### 2. APIs (Application Programming Interfaces)
Services that allow programs to request data directly.

Example:
Weather website provides temperature data through API.

API returns structured data (mostly JSON).

---

### 3. Web Pages
Information visible on websites but not directly downloadable.

Examples:
- product prices
- reviews
- rankings
- articles

Requires web scraping.

---

### 4. Files
Static datasets stored as:

- CSV
- Excel
- JSON
- Parquet

Often provided in public datasets.

---

### 5. Sensors & Logs
Automatically generated data:

- mobile app usage
- IoT devices
- server logs

Usually large and unstructured.

---

## Why Data Collection Matters in AI

Quality of model depends on quality of data.

Better data collection leads to:
- fewer missing values
- less bias
- more reliable predictions

Most AI effort is spent collecting and preparing data rather than training models.

---

## Mental Model

Data can exist in three forms:

Structured → Databases, APIs  
Semi-structured → JSON, logs  
Unstructured → HTML pages

Data collection techniques depend on data format.
