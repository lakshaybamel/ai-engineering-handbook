# Data Collection

Data collection is the first step of every Data Science and Machine Learning pipeline.

Before cleaning, analyzing, or training models — data must be gathered from real-world sources.

This module documents practical techniques used to obtain data from external systems.

---

## Position in AI Workflow

Raw World → **Data Collection** → Data Cleaning → Analysis → Feature Engineering → Machine Learning

If the collected data is wrong, every step after it becomes unreliable.

---

## Types of Data Sources

Different sources require different techniques:

| Source | Technique |
|------|------|
Databases | SQL Queries |
APIs | HTTP Requests |
Websites | Web Scraping |
Files | CSV / JSON loading |

This module focuses on APIs and Web Scraping.

---

## Module Contents

### 1. Data Sources
📂 [Data Sources](01-data-sources/README.md)

Concepts covered:
- population vs sample
- structured vs unstructured data
- where real-world data exists

---

### 2. Working with APIs
📂 [Working with APIs](02-working-with-apis/README.md)

Concepts covered:
- HTTP requests
- GET method
- JSON responses
- why APIs are preferred

---

### 3. HTML Basics for Scraping
📂 [HTML Basics](03-html-basics-for-scraping/README.md)

Concepts covered:
- HTML structure
- tags and attributes
- DOM tree
- webpage inspection

---

### 4. Requests Library
📂 [Requests Library](04-requests-library/README.md)

Concepts covered:
- downloading webpages
- headers
- status codes
- timeouts

---

### 5. BeautifulSoup
📂 [BeautifulSoup](05-beautifulsoup/README.md)

Concepts covered:
- parsing HTML
- finding elements
- extracting text and attributes

---

### 6. Advanced Scraping Techniques
📂 [Advanced Scraping](06-advanced-scraping-techniques/README.md)

Concepts covered:
- avoiding blocking
- delays
- pagination
- error handling

---

### 7. Storing Collected Data
📂 [Storing Data](07-storing-collected-data/README.md)

Concepts covered:
- saving JSON
- saving CSV
- preparing datasets for analysis

---

## Practical Notebook

📓 [Data Collection Notebook](notebooks/data_collection.ipynb)

The notebook demonstrates a complete pipeline:

1. Collect structured data using API
2. Collect unstructured data using scraping
3. Clean extracted data
4. Store dataset for analysis

---

## Key Learning Outcome

After completing this module you should understand:

- where data originates
- how programs communicate with servers
- how webpages can be converted into datasets
- difference between API and scraping
- how raw information becomes analyzable data

---

## Mental Model

Always prefer:

API → if available  
Scraping → only if necessary

Reliable data collection leads to reliable models.