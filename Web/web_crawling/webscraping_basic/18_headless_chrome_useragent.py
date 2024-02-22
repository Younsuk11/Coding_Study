# Headless모드는 CLI기반의 서버 OS에서도 Selenium을 통한 크롤링/테스트를 가능하게 만드는 멋진 모드지만, 
# 어떤 서버들에서는 이런 Headless모드를 감지하는 여러가지 방법을 쓸 수 있습니다.
# 아래 글에서는 Headless모드를 탐지하는 방법과 탐지를 ‘막는’방법을 다룹니다.(창과 방패, 또 새로운 창!)


from bs4 import BeautifulSoup
import time


from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
# headless chrome 의 user agent의 내용을 기본 사람이 사용하는 user agent로 변경 ____ like request에서 headers 할당하는 것처럼.


browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe",options = options) 
# 크롬드라이버를 직접 이용은 해야하나, option설정을 "headless"로 설정하여 백그라운드 실행됨.
browser.maximize_window()


url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"

browser.get(url)

defected_value = browser.find_element_by_id("detected_value")
print(defected_value.text)
browser.quit()


#DevTools listening on ws://127.0.0.1:51650/devtools/browser/7ee9c45c-6384-4d68-bef1-aba43cbe78e6
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/90.0.4430.93 Safari/537.36

## user-agent: headlessChrome_ 이기때문에 접근을 막을 수 있음...탐지를 막아야함...


## Headless 탐지 방지- user agent 값 변경한 상태
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36



## selenium 공부
# "selenium with python" 검색하기...
