# BeautifulSoup (Extracting Data from HTML)

After downloading a webpage using `requests`, we receive raw HTML.

Humans read the rendered page, but programs must understand the structure.

BeautifulSoup parses HTML and allows searching elements easily.

---

## Parsing HTML

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
```

Now `soup` represents the webpage structure (DOM tree).

---

## Finding Elements

### find()

Returns first matching element.

```python
title = soup.find("h1")
print(title.text)
```

### find_all()

Returns list of elements.

```python
prices = soup.find_all("p", class_="price")

for p in prices:
    print(p.text)
```

---

## Accessing Attributes

```python
link = soup.find("a")
print(link["href"])
```

---

## Nested Search

Elements exist inside other elements.

```python
product = soup.find("div", class_="product")
price = product.find("span", class_="price")
```

---

## Text Cleaning

HTML contains spaces and newline characters.

```python
text = title.text.strip()
```

---

## Common Methods

| Method    | Purpose            |
|-----------|--------------------|
| find      | first match        |
| find_all  | all matches        |
| text      | element content    |
| get       | attribute value    |
| strip     | clean spaces       |

---

## Why BeautifulSoup is Needed

HTML is complex and nested.<br>
String search is unreliable.

BeautifulSoup understands HTML structure.

---

## Mental Model

requests → download HTML<br>
BeautifulSoup → locate tags → extract data