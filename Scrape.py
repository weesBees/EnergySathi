import requests
from bs4 import BeautifulSoup

url = "https://greencoast.org/energy-conservation/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

paragraphs = soup.find_all("p")
content = [p.get_text() for p in paragraphs]

for paragraph in content:
    print(paragraph)
    print()  # Add an empty line between paragraphs
