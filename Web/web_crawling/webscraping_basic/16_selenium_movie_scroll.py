# 구글 영화 페이지_ 할인 하는 영화 목록 가져오기

# 단, 동적 페이지 이므로 selenium 사용하기 -현재 페이지(스크롤) 반영 될때마다 새로운 정보 추가.



from bs4 import BeautifulSoup

import time
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe")


browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies/top"

browser.get(url)

# 스크롤 내리기(지정한 위치로)
# 모니터의 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)") #1080 : 해당 윈도우 해상도 세로 값(1920 X 1080) _ 즉, 한페이지를 scrolldown하는 것.
# browser.execute_script("window.scrollTo(0,2080)")

## 화면 가장 아래로 스크롤 내리기 - 현재 창의 높이 만큼.(documnet.body.scrollHeight)
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

interval = 2 # 2초에 한번씩 내리기

# 내리기 전, 현재 문서 높이 가져와서 저장(초기값)
prev_height = browser.execute_script("return document.body.scrollHeight")

while True: 
    

    # 스크롤 가장 아래로 내림(현재 높이까지 스크롤 내리기)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    #페이지 로딩 대기
    time.sleep(interval)

    #내린 후,  현재 문서 높이 저장
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height == prev_height:
        break

    else: 
        prev_height = current_height

    

# 다른방법
# while True: 
#     # 내리기 전, 현재 문서 높이 가져와서 저장(초기값)
#     prev_height = browser.execute_script("return document.body.scrollHeight")

#     # 스크롤 가장 아래로 내림(현재 높이까지 스크롤 내리기)
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#     #페이지 로딩 대기
#     time.sleep(interval)

#     #내린 후,  현재 문서 높이 저장
#     current_height = browser.execute_script("return document.body.scrollHeight")
#     if current_height == prev_height:
#         break


# 페이지 정보는 selenium의 browser를 통한 직접 정보를 가져왔음. 
# print(browser.page_source)

soup = BeautifulSoup(browser.page_source, "lxml") #brwoser.page_source : requests의 res.text랑 동치

movies = soup.find_all("div", attrs = {"class" : "Vpfmgd"}) 
# attrs = {"class": value = ["a","b"]}  ==== 리스트에 해당되는 내용들 "a", b"(value값들)... 항목들을 모두 가져오게됨.

# print(len(movies)) 

for movie in movies:
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
    

    # 할인 후 가격 / 현재 가격
    price = movie.find("span", attrs = {"class" : "VfPpfd ZdBevf i5DZme"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs = {"class" : "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else: 
        # print(title, " : 할인 되지 않는 영화", f"현재 가격 : {price}")
        continue
    
    
    link = "https://play.google.com" +movie.find("div", attrs = {"class" : "vU6FJ p63iDd"}).a["href"]
    # link ="https://play.google.com" + movie.find("a", attrs = {"class" : "JC71ub"}).get_text()

    # print(title, price, link)
    print(f"제목: {title}")
    print(f"할인 전 금액  : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : {}".format(link))
    print("="*120)

browser.quit()