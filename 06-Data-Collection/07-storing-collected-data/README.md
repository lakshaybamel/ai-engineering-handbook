# Storing Collected Data

After scraping, data exists only in memory.

To use it later (analysis, ML), we must store it in a structured format.

Storage converts temporary data → reusable dataset.

---

## Common Storage Formats

| Format | Use Case |
|------|------|
CSV | tabular data |
JSON | nested data |
TXT | raw text |
Database | large persistent data |

For ML workflows, CSV and JSON are most common.

---

## Storing as CSV

```python
import csv

data = [
    ["name", "price"],
    ["Phone", "15000"],
    ["Laptop", "60000"]
]

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

Good for loading into Pandas.

---

## Storing as JSON

```python
import json

data = [
    {"name": "Phone", "price": 15000},
    {"name": "Laptop", "price": 60000}
]

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
```

Keeps hierarchical structure.

--

## Appending Data

When scraping pages:

```python
all_products.append(product)
```

Then save once after loop finishes.

Avoid writing file repeatedly.

---

## Data Cleaning Before Saving

Convert types:

```python
price = float(price)
rating = int(rating)
```

Structured storage prevents issues during analysis.

---

## Final Pipeline

1. Request page
2. Parse HTML
3. Extract fields
4. Store structured data
5. Load into Pandas

---

## Mental Model

Scraping collects information<br>
Storage converts it into dataset