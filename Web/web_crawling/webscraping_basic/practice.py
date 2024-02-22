import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=BFT&nil_profile=fix_similar&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

with open("estate.txt", "w", encoding="utf-8") as f: 
    f.write(soup.prettify())