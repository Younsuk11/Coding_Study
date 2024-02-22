# Beautifulsoup modul : html으로 적힌 웹 페이지 정보들을 가져올 수 있다.
# Limitation...... : JAVAScrip로 동적으로 생성된 정보들은... 가져올 수 없다. _동적 이벤트에 로 인한 사이트 업데이트에 대해 따라가면서 정보 추출 못함.
# Selenium 사용하는 이유
# 1. 자바스크립트가 동적으로 만든 데이터들..크롤링(스크랩핑)하기 위해서
# 2. 사이트의 다양한 HTML 요소에 클릭, 키보드 입력 등 , 이벤트를 주기 위해서.
# 업무자동화 가능

# pip install selenium

# 웹 드라이버 설치 _ chrome 드라이버 : 브라우저를 제어하기 위한 드라이버

from selenium import webdriver


#크롬드라이버 객체 생성
browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe")
browser.get("http://naver.com") # 객체를 통한 페이지 정보 가져오기

# 이 이후는 직접 terminal 실행으로 한줄한줄 직접 실행
#beautifulsoup처럼 정보 추출.
elem = browser.find_element_by_class_name("link_login")
elem.click() # 클릭하기

browser.back()#  / foward() / refresh()
# 검색창
elem = browser.find_element_by_id("query")
from selenium.webdriver.common.keys import Keys # key module가져오기
elem.send_keys("나도코딩") # 검색창에 key글자 입력하기 - key module없이도 가능
elem.send_keys(Keys.ENTER) # 검색창에 key로 ENTER날리기

#a tag가져오기
elem = browser.find_element_by_tag_name("a") # "a" element 처음 거만 가져오기
elem = browser.find_elements_by_tag_name("a") # "a" elements 모두 가져오기

for e in elem:
    e.get_attribute("href")  #soup: soup.attribute["href"]-dictionary 형식으로


#다음
browser.get("http://daum.net")
elem = browser.find_element_by_name("q") # 검색창 element가져오기
elem.send_keys("나도코딩")
# 주의_ 페이지 넘김이나 페이지가 다시 돌아오면, 해당 페이지는 이미 새로고침이라
# 할당된 elem는 같은 페이지가 아님. 따라서 현재 돌아온 페이지가 같아도 다시 element 할당이 필요함.

browser.back()
elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩")
# 버튼 element가져오기- by xpath
elem = browser.find_element_by_xpath(r"xpath복사한것")
elem.click()

browser.close() # 현재 탭만 종료
browser.quit() # 모든 탭 종료



### request과 다른점..... event 동작으로 달라진 페이지 내용에 대해 
# 매번 호출해서 써야함.+ 동적인 event key등 불러오기 불가.
# back, forward, click, keyboard입력등.

