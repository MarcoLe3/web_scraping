import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://httpbin.org/forms/post'
response = requests.get(url)

# Check status
if response.status_code == 200:
    print("Success!")
else:
    print("Failed to retrieve page")

soup = BeautifulSoup(response.text, 'html.parser')

form = soup.find("form")
inputs = form.find_all("input")

for input_tag in inputs:
    name = input_tag.get("name")
    input_type = input_tag.get("type")
    print(f"Field name: {name}, Type: {input_type}")