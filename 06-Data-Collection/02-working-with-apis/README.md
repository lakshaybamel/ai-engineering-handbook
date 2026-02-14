# Working with APIs

APIs (Application Programming Interfaces) allow programs to request data directly from servers.

Instead of manually downloading data from a website, we can ask the server for structured information.

APIs are the cleanest and most reliable way to collect data from the internet.

---

## How API Communication Works

Client (your program) → sends request → Server → sends response

The response usually comes in JSON format.

Example:
A weather app requests temperature data from weather server.

---

## HTTP Request

Most APIs work using HTTP protocol.

Common request types:

| Method | Purpose |
|------|------|
GET | retrieve data |
POST | send data |
PUT | update data |
DELETE | remove data |

For data collection we mostly use **GET**.

---

## Making a Request in Python

```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
```

---

## Checking Response Status

response.status_code

### Common Codes

| Code | Meaning        |
|------|----------------|
| 200  | success        |
| 404  | not found      |
| 500  | server error   |

---

## Reading Data

Most APIs return JSON.

```python
data = response.json()
print(data)
```

---

## Why APIs are Preferred

Compared to scraping:

- structured data
- stable format
- faster
- legal usage

Always use API if available before scraping.

---

## Mental Model

API = database over internet

Instead of SQL query, you send HTTP request.