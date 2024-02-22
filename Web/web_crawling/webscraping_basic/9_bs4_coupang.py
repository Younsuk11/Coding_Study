#쿠팡 사이트 정보 추츨

#3. "쿠팡" 강의 내용 확인 결과 일부 항목이 웹에서 접근했을 때와는 조금 다르게 가져오는듯 합니다. 확인 결과 화면 중 약 80% 는 정상, 20%는 페이지에 존재하지 않는 값을 가져옵니다. 
# (어쩌면 다음 페이지에 나오는 내용일 수도 있습니다) 
# 또한 80% 의 항목도 웹 페이지와는 달리 순서가 조금 뒤죽박죽 섞인듯 보입니다. 
# requests  만 써서 가져왔을 때 쿠팡에서 반환해주는 값에 차이가 있는듯한데,  
# selenium 을 통한 결과를 비교해볼 필요가 있어 보이네요. 
# 수업 시간에 결과 내용에 대해 전수 검사를 해볼 생각을 미처 해보지 못하여 내용에 오류가 있었던 점, 진심으로 사과 드립니다.

# 보충설명

#HTTP protocol를 통해서 server 요청 - HTTP Method : Get, Post
#Get : 누구나 볼 수 있게, URL에 적어서 보냄 
#           - 링크/np/search? 변수 =값&변수=값&변수=값  ____해당 요청 자료에 대한 값들을 URL에 포함시켜서 보냄.
#           - 한번에 보내는 정보 용량이 정해져있음.

#POST: HTTP message body에 적어서 보냄. - 안정성, 용량 제한이 없음.(회원가입, 게시판 글)
#           -URL를 바꿔서 요청한 자료를 보내는 것임 아님.//// URL을 그대로 일듯. 자체 Body 내용이 바뀌는 것.

import requests
from bs4 import BeautifulSoup
import re  #긴 내용의 형식을 "일정한"형식 입력을 통해 해당되는 내용들 일괄 찾기 가능

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
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
        print("<광고 상품을 제외합니다.>")
        continue# continue없으면 조건문 탈출 후 , 및의 코드 진행
    # for 문 다음 항목으로 넘어가기 - 애초에 조건문을 광고가 없다면 표시하고 있다면 표시 안하는 것로 해도 됨.
        

    name = item.find("div", attrs = {"class" : "name"}).get_text()
    #apple 제품 제외
    if "Apple" in name:
        print("<애플 상품 제외합니다.>")
        continue
    


    price = item.find("strong", attrs = {"class" : "price-value"}).get_text()# 가격
    
    
    #평점 - 단, 평점이 없는 상품일 경우.... 모든 item에 해당되는 text 내용이 없을 수도 있음.. 있는 것을 따로 분류해야함.(조건식)
    #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회- 조건문

    rating = item.find("em", attrs = {"class" : "rating"})
    
    if rating : # True : NONE이 아니라면
        rating = rating.get_text()
    else: 
        print("<평점 없는 상품 제외합니다.")
        continue


    #평점 수 
    rating_count =item.find("span", attrs = {"class" : "rating-total-count"})
    if rating_count : 
        rating_count = rating_count.get_text() # 출력 값: (number) - slicing하기 [a:b] : b직전까지
        rating_count_num= rating_count[1:-1] #앞에서 부터는 0~ 양수 / 맨뒤(-1) 직전까지
    else: 
        print("<평점 수가 없는 상품 제외합니다.")
        continue

    if float(rating) > 4.5 and int(rating_count_num) >100: 
        print(name, price)
        print("평점 : ", rating, "/","리뷰 수 :", rating_count)


    







