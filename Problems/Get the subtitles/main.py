import requests

from bs4 import BeautifulSoup

row = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
subtitles = soup.find_all("h2")

print(subtitles[row].text)

