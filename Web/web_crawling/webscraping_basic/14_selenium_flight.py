import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe")

browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"

browser.get(url) # url 로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# # 이번 달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # 이번달
# browser.find_elements_by_link_text("28")[0].click() # 이번달

# # 다음 달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # 다음달
# browser.find_elements_by_link_text("28")[1].click() # 다음달

# 이번 달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # 이번달
browser.find_elements_by_link_text("28")[1].click() # 다음달

browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/a[2]").click()
browser.find_element_by_link_text("제주").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()
# 일정 시간 로딩 화면 출력


# 첫번째 결과 출력
# 로딩시간 처리 :1. 시간기다리기(time.sleep(시간)) 2.element가 나올때까지(시간을 측정)

# 2. 해당(input) element가 나오면 시간 기다리기 종료. 그전까지는 webdriver가 기다리기(WebDriverWait)
# 해당 element 지정 input 방법 : ((튜플)) = ((By.XPATH, xpath주소)) - 여기서 By module 사용 / xpath말고도 id, class_name, link_text등 가능
try : 

    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)

finally:  # 기다린 시간(10초 설정) 시간전에 끝나게 되면, 종료하기.
    browser.quit()

# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# # problem : 항공권 검색 클릭 이후 , 로딩하는 시간 때문에 바로 실행 불가
# print(elem) # elem.text : 갖고 있는 텍스트값 반환.
