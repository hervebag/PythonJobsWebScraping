# Web Scraper: Data Extractor

This Python-based web scraper uses `requests` and `BeautifulSoup` to extract structured data from a paginated website and export it into a CSV file. It is designed to be simple and reusable.
The data extracted is from https://www.python.org/jobs/. The scraper filters for "Machine learning" jobs.
---

## 📌 Features

- Scrapes data across multiple pages
- Parses HTML content using `BeautifulSoup`
- Saves extracted data to a CSV file
- Lightweight with minimal dependencies

---

## 🧰 Technologies Used

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- CSV (built-in Python module)

---

## 🚀 Getting Started
Steps for running the script:
* Install dependencies: pip install -r requirements.txt
* Run the scraper: python WebScraper.py