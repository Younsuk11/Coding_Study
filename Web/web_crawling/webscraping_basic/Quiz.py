
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

#headless chrome
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")

browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe")
browser.maximize_window()


#다음 접속
url = "http://www.daum.net"
browser.get(url)
#검색창에 "송파헬리오시티" 검색
search = browser.find_element_by_id("q")
search.send_keys("송파 헬리오시티") 
search.send_keys(Keys.ENTER)

#스크롤 내리기(해당 element 찾을 때까지) - selenium
from selenium.webdriver import ActionChains
table = browser.find_element_by_xpath("//*[@id='estateColl']/div[3]/a/span")
action = ActionChains(browser)
action.move_to_element(table).perform()
# element가 보일때까지 : 해당 elem는 맨 아래 위치 하게 됨.
cur_height = browser.execute_script("return document.body.scrollHeight")


#부동산 부분 결과 정보 추출 및 출력 - beautifulsoup 
# dispaly noen 으로 숨겨진 table에서 정보 추출(selenium은 보여진 element에 대해서만) - click 을 통한 방법 비효율적?
# display = browser.find_element_by_id("estateCollTabLoading") # 보여지는 상태 바꾸기
# browser.execute_script("arguments[0].setAttribute('style', 'display:block;')", display)


# 보여주는 함수
def show_list_for_sale(xpath_input): 
    btn_sales = browser.find_element_by_xpath(xpath_input)
    browser.execute_script("arguments[0].click()", btn_sales) # btn_sales.click()
    time.sleep(1) # 동적 로딩 걸림.(상태 바뀌기 전, 프로그램실행시 반영x)

    soup = BeautifulSoup(browser.page_source, "lxml")
    sales = soup.find("table",attrs ={"class": "tbl"}).find("tbody").find_all("tr")

    for idx, sale in enumerate(sales):
        cols = sale.find_all("div", attrs ={"class": "txt_ac"})
        cols = [col.get_text().strip() for col in cols] # cols : 매물들의 값이 들어있는 리스트
        print(cols)

        if len(cols) >0:
            writer.writerow(cols)
            print("="*10,f"매물 {idx+1}","="*10)

            print(f"거래  : {cols[0]}")
            print(f"면적  : {cols[1]}(공급/전용)")
            print(f"가격  : {cols[2]}(만원)")
            print(f"동  : {cols[3]}")
            print(f"층  : {cols[4]}")
            
            print("")

        else:
            writer.writerow("")
            print("")

    writer.writerow("")

    #csv 파일 저장
    
        



## 각각 전체, 매매, 전세, 월세 테이블
file_name = "house_information.csv"
f = open(file_name, "w", encoding="utf-8-sig", newline ="")
writer = csv.writer(f)

title = "거래	공급/전용면적	매물가(만원)	동	층".split("\t")
writer.writerow(title)


#전체
xpath_of_whole = "//*[@id='estateCollInnerTab']/div/span[1]/a"
show_list_for_sale(xpath_of_whole)
#매매
xpath_of_sale = "//*[@id='estateCollInnerTab']/div/span[2]/a"
show_list_for_sale(xpath_of_sale)
#전세
xpath_of_lease = "//*[@id='estateCollInnerTab']/div/span[3]/a" # 매매가 찍힘
show_list_for_sale(xpath_of_lease)
#월세
xpath_of_monthly_rent = "//*[@id='estateCollInnerTab']/div/span[4]/a" # 전세가 찍힘
show_list_for_sale(xpath_of_monthly_rent)


time.sleep(1)
browser.quit()

