# 웹 페이지에서 이미지 자동 다운로드

import requests
from bs4 import BeautifulSoup
import re


#각 연도의 1위~ 5위의 영화 이미지 가져오기
for year in range(2016,2021 ): #2016 ~ 2020년까지
    
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs = {"class" : "thumb_img"})


    # 해당 연도 이미지 가져오기
    for idx, img in enumerate(images): # for문 탈출 조건  :  1위~ 5위까지만의 img만 가져오기
        if idx >=5: #상위 5개만 img가져오기
            break

        img_url  = img["src"]
        if img_url.startswith("//"): # method : startswith("문자열") : 해당 문자열로 시작하는지 여부 확인(boolean)
            img_url = "https:"+img_url
        

        #이미지 다운로드- 가져온 이미지 url주소 창으로 들어간 페이지에서 또 정보 가져와서, 갖고 있는 img 파일 저장.(with, pickle)
        image_res = requests.get(img_url)
        image_res.raise_for_status()
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f: # 여는 파일이 text파일이 아니기 때문에. mode=writing binary, encoding은 없어도 됌.
            f.write(image_res.content) # method : request.content = request받은 내용 (url)의 콘텐츠 : img파일을 가져옴.
            # 만약 파일명 연도별로 구분안하면, 같은 idx에 대해 파일이 덮어쓰게 됨.


# Project IDEA
## Project idea: GUI + bs4. webscrapping
# GUI에 필요한 조건 입력하여... 가격, 리뷰, 리뷰수 등.... 광고제거  혹은 제품 브랜드 ... 해동 조건의 제품들 목록 만들기.
#각 해당하는 img 저장하고, img 합치기.

