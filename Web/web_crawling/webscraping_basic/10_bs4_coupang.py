#쿠팡 정보 추출
# 최근 5페이지 정보 추출


import requests
from bs4 import BeautifulSoup
import re  #긴 내용의 형식을 "일정한"형식 입력을 통해 해당되는 내용들 일괄 찾기 가능

for i in range(1,6): # 1페이지 ~ 5페이지

    print("\"현재 {}페이지 입니다.\"".format(i))
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    # 쿠팡은 프로그램을 통해 접속하면 막음... user agent를 통해 사람이 접속하는 것처럼 해야함.

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    res = requests.get(url, headers= headers)
    # print(res.status_code)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # regular expression사용

    items = soup.find_all("li", attrs ={"class" : re.compile("^search-product")})
    # re.compile(^expression) : 문자열 앞부분이. expression에 해당하는 내용들 모두 찾기 vs. soup.find_all: 정확한 표현이 필요함.

    # print(items[0].find("div", attrs = {"class" : "name"}).get_text())

    for item in items : 

        # 광고 제품은 제외- 조건문
        add_badge = item.find("span", attrs = {"class" : "ad-badge"})
        if add_badge : 
            # print("<광고 상품을 제외합니다.>")
            continue# continue없으면 조건문 탈출 후 , 및의 코드 진행
        # for 문 다음 항목으로 넘어가기 - 애초에 조건문을 광고가 없다면 표시하고 있다면 표시 안하는 것로 해도 됨.
            

        name = item.find("div", attrs = {"class" : "name"}).get_text()
        #apple 제품 제외
        if "Apple" in name:
            # print("<애플 상품 제외합니다.>")
            continue
        


        price = item.find("strong", attrs = {"class" : "price-value"}).get_text()# 가격
        
        
        #평점 - 단, 평점이 없는 상품일 경우.... 모든 item에 해당되는 text 내용이 없을 수도 있음.. 있는 것을 따로 분류해야함.(조건식)
        #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회- 조건문

        rating = item.find("em", attrs = {"class" : "rating"})
        
        if rating : # True : NONE이 아니라면
            rating = rating.get_text()
        else: 
            # print("<평점 없는 상품 제외합니다.")
            continue


        #평점 수 
        rating_count =item.find("span", attrs = {"class" : "rating-total-count"})
        if rating_count : 
            rating_count = rating_count.get_text() # 출력 값: (number) - slicing하기 [a:b] : b직전까지
            rating_count_num= rating_count[1:-1] #앞에서 부터는 0~ 양수 / 맨뒤(-1) 직전까지
        else: 
            # print("<평점 수가 없는 상품 제외합니다.")
            continue

        if float(rating) > 4.5 and int(rating_count_num) >100: 
            print(f"제품명 :{name}" )
            print(f"가격 :{price}" )
            print(f"평점 :{rating}점 / 리뷰 수 : {rating_count}" )
            print("링크 주소 :", "http://www.coupang.com"+item.a["href"])
            print("-"*100)
            

## Project idea: GUI + bs4. webscrapping
# GUI에 필요한 조건 입력하여... 가격, 리뷰, 리뷰수 등.... 광고제거  혹은 제품 브랜드 ... 해동 조건의 제품들 목록 만들기.







