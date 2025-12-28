import requests
from bs4 import BeautifulSoup
import csv
import json
import os
os.makedirs("output", exist_ok=True)

BASE_URL = "https://quotes.toscrape.com"
url = "/"

all_quotes = []

while url:
    print("Scraping:", BASE_URL  + url)

    response = requests.get(BASE_URL + url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)

        tag_list = q.find_all("a", class_="tag")
        tags =",".join(t.get_text(strip=True) for t in tag_list)

        author_link = q.find("a")["href"]
        author_page = requests.get(BASE_URL + author_link)
        author_soup = BeautifulSoup(author_page.text, "html.parser")

        born_date = author_soup.find("span", class_="author-born-date").get_text(strip=True)
        born_location = author_soup.find("span", class_="author-born-location").get_text(strip=True)
        description = author_soup.find("div", class_="author-description").get_text(strip=True)

        all_quotes.append({
            "quote": text,
            "author": author,
            "tags": tags,
            "born_date": born_date,
            "born_location": born_location,
            "description": description
        })

    next_btn = soup.find("li", class_="next")
    url = next_btn.find("a")["href"] if next_btn else None


# Save JSON
with open("output/quotes.json", "w", encoding="utf-8") as f:
    json.dump(all_quotes, f, indent=2, ensure_ascii=False)

# Save CSV
with open("output/quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author", "Tags", "Born Date", "Born Location", "Description"])

    for q in all_quotes:
        writer.writerow([
            q["quote"],
            q["author"],
            q["tags"],
            q["born_date"],
            q["born_location"],
            q["description"]
        ])

print("Project Completed Successfully!")        
