import requests

from bs4 import BeautifulSoup

word = input()
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
paragraphs = soup.find_all("p")

for p in paragraphs:
    if word in p.text:
        print(p.text)
        break
