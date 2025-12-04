import requests
from bs4 import BeautifulSoup

def scrape_title(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.title.string
    print("Page Title:", title)

# Example
scrape_title("https://example.com")
