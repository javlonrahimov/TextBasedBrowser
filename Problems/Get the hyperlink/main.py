import requests

from bs4 import BeautifulSoup

act_no = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
links = soup.find_all("a")

print(links[act_no - 1].get("href"))
