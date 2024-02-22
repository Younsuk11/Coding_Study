import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")