# Requests Library (Downloading Web Pages)

After identifying a webpage, the next step is downloading its HTML.

Python cannot scrape directly from browser view — it must request the page from the server.

The `requests` library is used to communicate with web servers using HTTP.

---

## Basic Request

```python
import requests

url = "https://example.com"
response = requests.get(url)
```

This sends a GET request to the server and downloads the webpage.

---

## Understanding the Response Object

The server sends back a response containing multiple parts.

### Status Code

```python
response.status_code
```

### Common Codes

| Code | Meaning                 |
|------|-------------------------|
| 200  | success                 |
| 403  | forbidden (blocked)     |
| 404  | page not found          |
| 500  | server error            |

Always check status before parsing.

---

## Page Content

Raw HTML:

```python
html = response.text
print(html[:500])
```
This is what the scraper reads.

---

## Headers (Important)

Many websites block unknown programs.

Browsers send identity information called headers.

Without headers → request may fail.

Example:

```python
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
```

This makes the request look like a real browser.

---

## Handling Errors

Never assume request always works.

```python
if response.status_code == 200:
    html = response.text
else:
    print("Request failed")
```

---

## Timeout (Prevent Hanging)

Some servers never respond.

```python
response = requests.get(url, timeout=5)
```

Stops request after 5 seconds.

---

## Rate Limiting (Politeness)

Rapid requests may block your IP.

```python
import time
time.sleep(2)
```

Always add delay in loops.

---

## What Requests Does NOT Do

Requests only downloads HTML.<br>
It does not extract data.

Extraction is done using BeautifulSoup.

---

## Mental Model

requests → download page<br>
BeautifulSoup → read page