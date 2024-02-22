# 가우스 전자 
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url) 
res.raise_for_status() 

soup = BeautifulSoup(res.text, "lxml") 


cartoons = soup.find_all("td", attrs = {"class": "title"})


# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]

# print(title, "https://comic.naver.com" +link)

# 웹페이지 타이틀, 링크 정보 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)

rate_cartoons = soup.find_all("div", attrs = {"class": "rating_type"})


total_rates =0 # (초기값)
# 평점 구하기 
for cartoon in rate_cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수:", total_rates)
print("평균 점수: ",total_rates / len(cartoons))


# /html/body/div/div[3]/div[1]/table/tbody/tr[1]/td[2]/a
# /html/body/div/div[3]/div[1]/table/tbody/tr[1]/td[3]/div/strong

# Q: 한꺼번에 하기 title, link, 평점. - parent 속 각각의 성분 빼오기....


##terminal 창에서 python을 통해 직접 실행 가능

## beautifulsoup Documentation 이용해서 beautifulsoup module 이용해보기

