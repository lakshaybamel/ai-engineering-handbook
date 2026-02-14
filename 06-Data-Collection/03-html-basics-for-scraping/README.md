# HTML Basics for Scraping

Web scraping works by reading the structure of a webpage.

A webpage is not just text — it is structured using HTML (HyperText Markup Language).

Scraping means extracting data from this structure.

---

## How a Webpage is Built

A webpage consists of nested elements called tags.

Example:

```html
<html>
  <body>
    <h1>Product Title</h1>
    <p class="price">₹999</p>
  </body>
</html>
```

The browser shows formatted content
Scraper reads raw HTML structure

---

## Important Tags

| Tag        | Meaning           |
|------------|-------------------|
| h1, h2, h3 | headings          |
| p          | paragraph         |
| a          | link              |
| img        | image             |
| table      | tabular data      |
| div        | container         |
| span       | inline container  |

Scraping focuses on locating correct tags.

---

## Attributes
Tags often contain extra information.

Example:

```html
<p class="price">₹999</p>
<a href="/product/1">View</a>
```

| Attribute | Purpose           |
|-----------|-------------------|
| class     | group elements    |
| id        | unique element    |
| href      | link destination  |
| src       | image source      |

Scrapers use attributes to locate elements.

---

## DOM Structure

HTML forms a tree structure (Document Object Model).

Parent → Child → Sibling relationships

Understanding hierarchy helps target correct data.

---

## Inspecting a Webpage

In browser:<br>
Right click → Inspect

You can view:

- tag name
- class
- id
- nesting

Scraping always starts with inspection.

---

## Mental Model

Website view → human readable<br>
HTML source → machine readable

Web scraping reads the source, not the visual layout.