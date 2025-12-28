# Python Web Scraping Project – Quotes Website

This project demonstrates a complete end-to-end web scraping workflow using Python and BeautifulSoup.  
Data is scraped from https://quotes.toscrape.com including pagination and nested author details.

This project is designed for learning, portfolio showcase, and freelancing platforms such as Fiverr and Upwork.

---

## 🔧 Technologies Used
- Python
- requests
- BeautifulSoup (bs4)
- CSV
- JSON

---

## 📄 Features
- Scrapes all quotes from all pages (pagination supported)
- Extracts:
  - Quote text
  - Author name
  - Tags
- Performs nested scraping:
  - Visits each author page
  - Collects author born date
  - Collects author born location
  - Collects author description
- Saves data into:
  - CSV file
  - JSON file
- Clean, structured, and reusable code
- Beginner-friendly project structure

---

## 📂 Project Structure
python-web-scraping-quotes/
│
├── day9_scraper.py
├── requirements.txt
├── README.md
└── output/
├── quotes.json
└── quotes.csv

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kannezfatema/python-web-scraping-quotes.git
cd python-web-scraping-quotes

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Script
python day9_scraper.py

📁 Output Files
output/quotes.csv
Contains the following columns:
> Quote
> Author
> Tags
> Born Date
> Born Location
> Description

output/quotes.json
Structured JSON data with nested author details.

🎯 Use Cases
> Web scraping practice
> Data collection and analysis
> Automation projects
> Freelancing portfolio (Fiverr / Upwork)
> Beginner to intermediate Python scraping reference

🧠 Skills Demonstrated
> HTTP requests handling
> HTML parsing with BeautifulSoup
> Pagination handling
> Nested data scraping
> Data cleaning
> CSV and JSON file handling
> Python scripting best practices

👩‍💻 Author
Kannez Fatema
Python Web Scraping Learner & Freelancer

⚠️ Disclaimer
This project is for educational and portfolio purposesonly.
Always check and respect a website’s terms of service before scraping.

⭐ Support
If you find this project helpful, consider giving it a ⭐ on GitHub!
