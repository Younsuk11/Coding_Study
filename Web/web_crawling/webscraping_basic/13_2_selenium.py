# 자동 로그인
import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe")
browser.get("http://naver.com")


# 1. 로그인 링크 들어가기
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
# element를 가져와서 변수 객체와 시키지 않고 바로 해당 객체에 내용 입력 

browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭

browser.find_element_by_class_name("btn_global").click()

#문제점. 프로그램을 통한 로그인은 : 사람이 아닌것으로 간주, 자동입력 방지 문자 입력을 해야함.
# User agent를 사용해야함.

# 5. id 새로 입력
time.sleep(3)
browser.find_element_by_id("id").clear() # 해당 element 안에 담겨있는 내용 지우기
browser.find_element_by_id("id").send_keys("my_id") 

# 6. html 정보 출력

print(browser.page_source) # F12에 대한 정보 가져오기. - 이후 Beautifulsoup 활용

# 7. 브라우저 종료
browser.quit() # 전체 브라우저 종료

