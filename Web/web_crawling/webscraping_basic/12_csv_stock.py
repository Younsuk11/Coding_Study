#csv: comma separated value

import csv
import requests
from bs4 import BeautifulSoup
import re

filename = "시가총액(1-200).csv"
#파일 열기
f = open(filename, "w", encoding  = "utf-8-sig", newline = "") #input : newline = ""_  줄바꿈 newline을 공백으로 / 엑셀파일 한글로 쓴 내용 깨질때는 encoding바꿔주기
writer = csv.writer(f) # csv파일에 쓰기

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
#method : split("input") : input값을 기준으로 각각 나눈 것들을 list형식으로 저장

writer.writerow(title)#column 제목 넣기

for page in range(1,2) : # 1~ 4page 내용
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs = {"class" : "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <=1 : # 의미 없는 데이터(빈줄들.) skip
            continue

        #순위, 종목명, 현재가... 등
        data = [column.get_text().strip() for column in columns]# 각 항목들 값 내 공백지우기 : method : strip() 의미 없는 공백들 지우기
        # print(data)

        #* strip("char"): char에 포함된 모든 문자 및 그에 해당되는 조합들 양쪽에서 , 지우기 _ 공백 NONE일 경우,_ 공백 지우기
        # lstrip("char") : 선행되는(left) char에 해당되는 내용만, 지우기
        # rstrip("char") : 후행문자(right) char에 해당되는 내용만, 지우기

        writer.writerow(data) #input값: 리스트형으로 각각의 value가 구분된 형식



