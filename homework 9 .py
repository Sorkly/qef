
import requests

book_titles = []

response = requests.get("https://books.toscrape.com/catalogue/page-1.html")
response_text = response.text

response_parse = response_text.split("<li>")

for part in response_parse:
    if 'title="' in part:
        start = part.find('title="') + len('title="')
        end = part.find('"', start)
        title = part[start:end]
        book_titles.append(title)

for title in book_titles:
    print(title)