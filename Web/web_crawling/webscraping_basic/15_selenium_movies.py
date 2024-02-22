# 구글 영화 페이지_ 할인 하는 영화 목록 가져오기

# 단, 동적 페이지 이므로 selenium 사용하기 -현재 페이지(스크롤) 반영 될때마다 새로운 정보 추가.

import requests
from bs4 import BeautifulSoup


url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept-Language" : "ko-KR,ko" # 한글페이지 반환 요청.
    }

#headers = {"User-Agent": "에이전트 정보"}

res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs = {"class" :"ImZGtf mpg5gc"})
print(len(movies)) # 현재 10개임.


# with open("movies.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력

## 문제점... 접속하는 사용자(user agent)의 header를 통해서_ 페이지 정보를 줌.__ 즉 실제로 브라우저로 직접 접속할 때랑, 프로그램으로 접속의 header가 다를듯.
## 10개밖에? - request를 통한 정적 페이지(현재 스크롤)에 대해서만 정보 추출이 가능.....
#### 스크롤이 내려갈 때마다 갱신되는 페이지: 동적 페이지 - selenium 사용해야함.

# 10개 한정 (정적) : 제목 가져오기.
for movie in movies:
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
    print(title)





