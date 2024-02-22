# pip install beautiful4(package) , lxml

import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url) # 링크에 해당되는 웹 페이지의 전체 내용 가져와서 변수화
res.raise_for_status() # 링크 접근이 정상이 아니라면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml") # 가져온 내용 res의 문서(txt형식의 내용들)를 lxml(parser)를 통해 객체화(soup)
# lxml parser : xml로 이루어진 파일들(html, docx,xlsx, pptx등)을 해석하는 프로그램

# print(soup.title) 
# print(soup.title.get_text())

# print(soup.a)
# ## 현재 "soup"은 resquests로 가져온 res의 모든 문서 내용을 가지고 있음.
# ## soup(객체)에서 처음 발견되는 "a"에 해당되는 첫번째 내용

# print(soup.a.attrs) ##a element의 attributes(value)들을 보여줌.-dictionary
# print(soup.a["href"]) # a element의 href에 해당되는 value를 보여줌.

# #_______________이런 방식은 웹페이지 정보를 잘 알고 있을 떄 가능

# print(soup.find("a", attrs = {"class": "Nbtn_upload"}))
# ## 속성 attribute값(class : Nbtn_upload)에 해당하는 처음으로 발견되는 a element찾기

# print(soup.find(attrs = {"class": "Nbtn_upload"} ))
# ## 만약 class값이 있는 해당 element 찾기

# print(soup.find("li", attrs = {"class": "rank01"}))

# rank1 = soup.find("li", attrs = {"class" : "rank01"})

# print(rank1.a.get_text()) ## 객체화(변수화)를 통해서 갖고 있는 a element에 대한 내용 가져오기

#### 이 모든것은 python이 객체지향형 성격을 갖고 있기 때문.
#############################################
# soup : xpath처럼 (/html/body/div/span/a...) 부모 자식 관계를 통해 가져올 수 잇음

# 형제 element넘어가기
# print(rank1.next_sibling) ## .바로 next_sibling이 줄바꿈임.
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling ## rank3 기준으로 전전, 형제 element로 


# # 부모 element로 넘어가기
# print(rank1.parent)

# # 만약에 줄바꿈이 없을 수 도 있지 않나...? : 객체.find_next_sibling(조건)  :  조건에 해당하는 형제 , 부모 element찾기
# rank2 = rank1.find_next_sibling("li") # "li"에 해당하는 rank1의 기준의 다음 형제를 찾아서 객체화
# print(rank2.a.get_text())


# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

## 한번에 모든 정보 일괄 찾기

# ranks = rank1.find_next_siblings("li")
# print(ranks)

webtoon = soup.find("a", text ="소녀의 세계-2부 54화") 
## 객체 soup에서 가져온 정보들 중 처음으로 찾은 a에서 text내용(<여는 tag -내용> text </닫는 tag>)

# <a onclick="nclk_v2(event,'rnk*p.cont','654774','2')" href="/webtoon/detail.nhn?titleId=654774&amp;no=271" title="소녀의 세계-2부 54화">소녀의 세계-2부 54화</a>

print(webtoon)

