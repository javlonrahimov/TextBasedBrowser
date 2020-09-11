import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore

args = sys.argv
directory_name = args[1]
history = deque()
saved_tabs = []

if not os.path.exists(directory_name):
    os.makedirs(directory_name)


def extract_title(url):
    return str(url)[0:str(url).rfind('.')]


def parse_html(request):
    soup = BeautifulSoup(request.content, "html.parser")
    lines = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "ul", "ol", "li"])
    result = ""
    for line in lines:
        if line.name == "a":
            print(Fore.BLUE, line.text)
        else:
            print(line.text)

        result += line.text
    return result


while True:
    web_url = input()
    if '.' in web_url:
        if web_url == "exit":
            break
        elif web_url == 'back':
            history.pop()
            print(history.pop())
        else:
            r = requests.get(f'https://{web_url}')
            print(parse_html(r))
            with open(f'{directory_name}\\{extract_title(web_url)}.txt', 'w', encoding='utf-8') as f:
                f.write(parse_html(r))
                history.append(r.text)
                saved_tabs.append(extract_title(web_url))

    else:
        if web_url == "exit":
            break
        elif web_url == 'back':
            history.pop()
            print(history.pop())
        elif web_url in saved_tabs:
            with open(f'{directory_name}\\{web_url}.txt', 'r', encoding='utf-8') as f:
                print(f.read().replace('\n', ''))
        else:
            print("Error")