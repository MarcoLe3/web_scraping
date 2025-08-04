import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'http://quotes.toscrape.com'
response = requests.get(url)

# Check status
if response.status_code == 200:
    print("Success!")
else:
    print("Failed to retrieve page")

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for quote, author in zip(quotes, authors):
    print(f"{quote.text} — {author.text}")