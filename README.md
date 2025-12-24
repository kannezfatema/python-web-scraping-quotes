# Python Web Scraping Project – Quotes Website

This project demonstrates web scraping using Python and BeautifulSoup.
Data is collected from https://quotes.toscrape.com with pagination and nested scraping.

## 🔧 Technologies Used
- Python
- requests
- BeautifulSoup
- CSV
- JSON

## 📄 Features
- Scrape quotes, authors, and tags
- Handle pagination (all pages)
- Save data to CSV file
- Save nested author data to JSON file
- Clean and structured output

## 📂 Files
- day5_quotes_csv.py  
  → Scrapes all quotes and saves them to `quotes.csv`

- day6_quotes_json.py  
  → Scrapes quotes + author details (born date, location, description)  
  → Saves data to `quotes.json`

## ▶️ How to Run
```bash
pip install requests beautifulsoup4
python day5_quotes_csv.py
python day6_quotes_json.py
# python-web-scraping-quotes
Python web scraping project using BeautifulSoup
