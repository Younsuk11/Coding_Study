## headless chrome  : chrome창을 띄우지 않고 background로 동작을 실행 _  보다 빠른 처리 가능

from bs4 import BeautifulSoup

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe",options = options) 
# 크롬드라이버를 직접 이용은 해야하나, option설정을 "headless"로 설정하여 백그라운드 실행됨.

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

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")  #해당 브라우저 스크린샷 파일 저장


soup = BeautifulSoup(browser.page_source, "lxml") #brwoser.page_source : requests의 res.text랑 동치
    
movies = soup.find_all("div", attrs = {"class" : "Vpfmgd"}) 


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