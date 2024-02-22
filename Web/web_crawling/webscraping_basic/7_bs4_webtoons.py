## 웹툰 페이지 내용 모두 가져오기

# pip install beautiful4(package) , lxml

import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url) 
res.raise_for_status() 

soup = BeautifulSoup(res.text, "lxml") 

cartoons = soup.find_all("a", attrs = {"class" : "title"}) # find_all: 조건에 해당하는 모든 것.
#class : title이 들어간 모든 "a" element를 찾아옴.

#<네이버 웹툰 전체 목록 가져오기>
for cartoon in cartoons:

#가져온 모든 a element에서 text성분만 추출
    print(cartoon.get_text()) 





