# Advanced Scraping Techniques

Basic scraping works only on simple websites.

Real websites detect bots and may block requests.  
To scrape reliably, additional techniques are required.

---

## 1. Use Headers (Avoid Blocking)

Servers check if request comes from browser.

Without headers → 403 Forbidden

```python
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
```

This mimics a real browser.

---

## 2. Handle Request Failures

Websites may temporarily fail.

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException:
    print("Failed to fetch page")
```

Prevents program crash.

---

## 3. Add Delay Between Requests

Rapid requests look like bot activity.

```python
import time
time.sleep(2)
```

Prevents IP blocking.

---

## 4. Looping Over Pages (Pagination)

Many sites split data across pages.

Example:

```python
for page in range(1, 6):
    url = f"https://example.com/page={page}"
    response = requests.get(url, headers=headers)
```

---

## 5. Cleaning Extracted Data

Scraped data often messy.

```python
price = price.replace("₹", "").strip()
rating = float(rating)
```

---

## 6. Respect Robots.txt

Websites specify allowed scraping paths.

Always check:

```
https://example.com/robots.txt
```

Avoid restricted endpoints.

---

## When Scraping Fails

Common reasons:

| Problem       | Cause                     |
|---------------|---------------------------|
| 403 error     | missing headers           |
| empty page    | dynamic JS content        |
| random blocks | too many requests         |

Dynamic websites require tools like Selenium (not covered here).

---

## Mental Model

Simple site → direct scrape<br>
Protected site → mimic browser behavior