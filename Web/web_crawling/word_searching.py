import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import numpy as np
import time


def English_Korea(words):
        
        #input word 모두 소문자로 바꾸기
    words = [word.lower() for word in words]
        
    dictionary = {}
    synonyms = []
        
    url = "https://dic.daum.net/index.do?dic=eng"
        
    browser.get(url)
    for word in words:
        syns = [] #단어 개별, 유의어 리스트
            
        elem = browser.find_element_by_id("q")
        elem.clear()
        elem.send_keys(word)
        elem.send_keys(Keys.ENTER)

        soup = BeautifulSoup(browser.page_source, "lxml")

        cleanword = soup.find("strong", attrs = {"class": "tit_cleansch"})

        if cleanword:  #page 2 상태
            elem = browser.find_element_by_class_name("tit_cleansch")

            elem.click()# cleanword 클릭
                
            soup = BeautifulSoup(browser.page_source, "lxml")  #페이지 갱신(page2 -->)

        ## 검색결과가 없는 경우도 있음.... ---> AttributeError 에러처리 해야함...

        similar_words = soup.find("ul", attrs = {"id" : "SIMILAR_WORD"}) # 유의어 있을 때 사용
            
        if similar_words: #유의어가 있는 상태
            similar_words = similar_words.find_all("li")
                

            for i in range(len(similar_words)): # 세개만 저장 x --- 2개 이하 인 경우도 있음.
                syns.append(similar_words[i].a.get_text())# 리스트 형태
        
            synonyms.append(syns)  
        else: #유의어가 없거나 _ 스펠링이 틀린 경우
            
            synonyms.append("\"No Synonyms or Spelling is wrong\"")

    for index, word in enumerate(words):
        dictionary[word] = synonyms[index]

    browser.quit()
    for key, value in dictionary.items():
        print(key, ":", value)
        print("")

    return 

def English_English(words):
    words = [word.lower() for word in words]

    dictionary = {}
    meaning = []

    url = "https://dic.daum.net/index.do?dic=ee"
    browser.get(url)
        

    for word in words:
        elem = browser.find_element_by_id("q")
        elem.clear()
        elem.send_keys(word)
        elem.send_keys(Keys.ENTER)

        soup = BeautifulSoup(browser.page_source, "lxml")

        cleanword = soup.find("strong", attrs = {"class": "tit_cleansch"})

        if cleanword:  #page 2 상태에 있는 경우,
            elem = browser.find_element_by_class_name("tit_cleansch")
            elem.click()# cleanword 클릭
            soup = BeautifulSoup(browser.page_source, "lxml")  #페이지 갱신(page2 -->)



        txt_mean = soup.find("span", attrs = {"class" : "txt_mean"})


        if txt_mean : #영영 풀이가 있다. = 단어 검색이 된다.
            txt_mean = txt_mean.find_all("daum:word")
            texts= [text.get_text() for text in txt_mean]

            mean = ""
            for index in range(len(texts)):
                mean += " "+texts[index]

            meaning.append(mean)

        else: 
            meaning.append("\"Warning _ Spelling is wrong\"")

    for index, word in enumerate(words):
        dictionary[word] = meaning[index]

    # 한줄씩 출력하기'
    browser.quit()
    for key, value in dictionary.items():
        print(key, ":", value)
        print("")

    return

#browser options
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")


start = True
while start:
    print("=============================")
    print("#검색할 단어들을 입력해주세요#")
    print("Option > \n1.단어간 구별은 띄어쓰기로, 숙어는 \"-\"을 이용해주세요\n2.프로그램 종료를 원하시면 \"end\"를 입력하세요")

    words = input("Words : ").lower()
    if words == "end":
        break

    words = words.split() # 엔터나, 공백 기준 분활_리스트 저장
    
    
    state = True
    while state:

        print("=============================")
        print("1.English_synonym\n2.English_English\n종료 : \"end\"")
        command = input("사용하실 사전의 번호를 입력하주세요 : ").lower() ## string임

        
        if command =="1":
            browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe", options = options)
            state = False # 탈출
            English_Korea(words)
        elif command =="2":
            browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe", options = options)
            English_English(words)
            state = False

        elif command == "end": # 아예 종료
            start = False
            break

        else:
            print("====================================")
            print("*Warning : Command 입력이 틀렸습니다.")
            print("")
            continue
            


## 버그 및 추가사항

#* 버그 : 단어가 없으면(스펠링 오류시) 출력 내용이 없어서 프로그램 중단.---눈으로 확인하면서 처리해야한다는 불편함.  ---에러 처리
# 추가 : 찾을 단어 목록을 메모장에 넣어놓으면 (혹은 gui list) _ 해당 단어들 함수 돌려서 찾는다.___ gui button command
# 계속해서 프로그램 종료하지 않고 진행 -while