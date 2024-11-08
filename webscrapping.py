# -*- coding: utf-8 -*-
"""webscrapping

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AHPXOp87rKM4KRAxupeU-8hlSgtozzzO
"""

import requests
from bs4 import BeautifulSoup


base_url = "http://quotes.toscrape.com"
page_url = "/page/1"

while page_url:

    response = requests.get(base_url + page_url)
    soup = BeautifulSoup(response.content, "html.parser")

    quotes = soup.find_all("span", class_="text")
    for quote in quotes:
        print(quote.text)


    next_button = soup.find("li", class_="next")
    if next_button:

        page_url = next_button.find("a")["href"]
    else:

        page_url = None

import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://quotes.toscrape.com"
page_url = "/page/1"

with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    while page_url:
        response = requests.get(base_url + page_url)
        soup = BeautifulSoup(response.content, "html.parser")

        quotes = soup.find_all("div", class_="quote")
        for quote in quotes:
            quote_text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]
            tags_str = ", ".join(tags)

            writer.writerow([quote_text, author, tags_str])

        next_button = soup.find("li", class_="next")
        page_url = next_button.find("a")["href"] if next_button else None

print("Scraping completed! Data saved to quotes.csv.")

