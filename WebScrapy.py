import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    response = requests.get(url)
    response.raise_for_status() 
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = []
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        titles.append(heading.get_text(strip=True))
    return titles

if __name__ == "__main__":
    url = "https://webscraper.io/test-sites"  # Replace with your target website
    titles = scrape_titles(url)
    for idx, title in enumerate(titles, 1):
        print(f"{idx}. {title}")