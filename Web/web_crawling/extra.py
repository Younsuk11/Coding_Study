# 1. 단어 자동 검색 - 한영(유의어들) + 영영(definition)
import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import numpy as np
import time


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")

browser = webdriver.Chrome(r"C:\Users\user\Desktop\programming\python\chromedriver_win32\chromedriver.exe",options = options)


class Personal_Dictionary: 

    def __init__(self, words):
        self.words = words
        

    
    def English_English(self):
        self.words = [word.lower() for word in self.words]
        meaning = []
        dictionary = {}
        

        url = "https://dic.daum.net/index.do?dic=ee"
        browser.get(url)

        for word in self.words:
            elem = browser.find_element_by_id("q")
            elem.clear()
            elem.send_keys(word)
            elem.send_keys(Keys.ENTER)

            time.sleep(0.4)
            
            soup = BeautifulSoup(browser.page_source, "lxml")

            cleanword = soup.find("strong", attrs = {"class": "tit_cleansch"})

            if cleanword:  #page 2 상태에 있는 경우,
                elem = browser.find_element_by_class_name("tit_cleansch")

                elem.click()# cleanword 클릭
                
                soup = BeautifulSoup(browser.page_source, "lxml")  #페이지 갱신(page2 -->)

            txt_mean = soup.find("span", attrs = {"class" : "txt_mean"}).find_all("daum:word")
            texts= [text.get_text() for text in txt_mean]

            mean = ""
            for index in range(len(texts)):
                mean += " "+texts[index]

            meaning.append(mean)

        for index, word in enumerate(self.words):
            dictionary[word] = meaning[index]

        browser.quit()

        for key, value in dictionary.items():
            print(key, ":", value)
            print("")

        return 
    

    
    def English_Korea(self):
        
        #input word 모두 소문자로 바꾸기
        self.words = [word.lower() for word in self.words]
        
        dictionary = {}
        synonyms = []
        
        url = "https://dic.daum.net/index.do?dic=eng"
        
        browser.get(url)
        for word in self.words:
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

            similar_words = soup.find("ul", attrs = {"id" : "SIMILAR_WORD"}) # 유의어 있을 때 사용
            
            if similar_words: #유의어가 있는 상태
                similar_words = similar_words.find_all("li")
                

                for i in range(0,3): # 세개만 저장
                    syns.append(similar_words[i].a.get_text())# 리스트 형태
        
                synonyms.append(syns)  
            else: #유의어가 없을 때
            
                synonyms.append("None")

        for index, word in enumerate(self.words):
            dictionary[word] = synonyms[index]

        browser.quit()
        for key, value in dictionary.items():
            print(key, ":", value)
            print("")

        return 

    


##input으로 딕셔너리의 key값들을 넘겨줌 __ 함수는 key값의 value를 채운 후 반환.
# words = ["suppress", "cripple","spruce", "firs", "lee", "forunate", "burrow", "leached into", "manure", "den", "forage"]
words = ["specular", "overindulgence", "engraving", "etherealness", "inlaid", "effervescence", "cherub"]
PD = Personal_Dictionary(words)
PD.English_English()
# PD.English_Korea()

