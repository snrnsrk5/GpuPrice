import requests
from bs4 import BeautifulSoup

def Won(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.select_one('span[class=value]').string

    t = tag[0:1]
    h = tag[2:5]
    w = t+h

    return int(w)
    