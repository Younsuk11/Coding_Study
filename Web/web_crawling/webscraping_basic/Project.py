# 나만의 비서 프로그램-한번에 여러 페이지 접속
import requests
from bs4 import BeautifulSoup
from datetime import datetime


#1. 네이버 "오늘" 서울의 날씨
def today_weather(location_number):
    url1 ="https://weather.naver.com/today/{}".format(location_number) #09290125 : 위치정보
    
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")

    #위치
    location_name = soup1.find("strong", attrs = {"class" : "location_name"}).get_text()

    #weather_area : 흐림, 어제보다, 현재(최저, 최고)
    weather_area = soup1.find("div", attrs = {"class" : "weather_area"})
    #현재 기상상태
    cur_weather = weather_area.find("span", attrs = {"class" :"weather before_slash"})
    
    
    #어제랑 비교(같은 경우, 다른경우 나눠야 함.) : method: get() - 없으면 none리턴
    differ_yes = weather_area.find("p", attrs = {"class": "summary"}).find_all("span")
    if len(differ_yes) == 1:
        differ_yes = "어제와 같은 기온"
    else: 
        differ_yes = "어제보다 "+ differ_yes[0].get_text()


    #현재 온도
    cur_temperature = weather_area.find("span", attrs= {"class" : "blind"}).next_sibling
    
    
    #최저. 최고 : 가장 맨 위에것.
    lowest_temp  = soup1.find("span", attrs = {"class" : "lowest"}).find("span").next_sibling
    highest_temp = soup1.find("span", attrs = {"class" : "highest"}).find("span").next_sibling
    
    #soup 확률 평균내기
    rain_percentages = soup1.find("tr", attrs = {"class" : "row_icon"}).find_all("td")
    # "오늘" 24시간 안으로 계산 된것들만.
    time_td = datetime.today().strftime("%Y%m%d")
    td_rain_pers_morning = [] # "오늘" 날짜인 오전 element들
    td_rain_pers_afternoon = []
    for rain_percentage in rain_percentages:
        
        if int(rain_percentage["data-ymdt"][:-2]) == int(time_td):#"오늘"날짜만

            if int(rain_percentage["data-ymdt"][-2:]) <= 12: # 시각 오전 오후 나눔.
                td_rain_pers_morning.append(rain_percentage.em.get_text())
            else:
                td_rain_pers_afternoon.append(rain_percentage.em.get_text())
        else:
            continue
    # print(td_rain_pers_morning, td_rain_pers_afternoon)
    try :
        per_morning = round((sum(float(per) for per in td_rain_pers_morning) / len(td_rain_pers_morning)),1)
    except ZeroDivisionError:
        per_morning = "확률 계산중입니다."
        
    try:
        per_afternoon = round((sum(float(per) for per in td_rain_pers_afternoon) / len(td_rain_pers_afternoon)),1)
    except ZeroDivisionError:
        per_afternoon = "확률 계산중입니다."
    
    #미세먼지 - 페이지 넘어가기(reqeust로는 어떻게 페이지 넘기지???- 페이지 주소 바꾸기... 한계가 있을듯.
    url1 = "https://weather.naver.com/air/{}".format(location_number)
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    dusts = soup1.find_all("em", attrs = {"class":"grade"})
    fine_dust = [dusts[0].get_text(),dusts[0].next_sibling]
    ##* 부모 tag의 text추출하기 (항상 그냥get_text()는 자식 text까지 추출 )
    ##### text자체도 어떤 tag의 형제관계일 수 있음 단 이때는 tag가 아니무로 get text()x
    micro_dust = [dusts[1].get_text(),dusts[1].next_sibling]



    print(f"[오늘의 날씨 - {location_name}]\n")
    print(f"{cur_weather.get_text()}, {differ_yes}")
    print(f"현재 {cur_temperature}° (최저 {lowest_temp} / 최고 {highest_temp})")
    print(f"오전 강수 확률 : {per_morning}% / 오후 강수 확률 : {per_afternoon}%")
    print("")
    print(f"미세먼지 {fine_dust[1]}μg/m^3 {fine_dust[0]}")
    print(f"초미세먼지 {micro_dust[1]}μg/m^3 {micro_dust[0]}")



def news():
    #헤드라인 뉴스 3건
    url = "https://news.naver.com/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

    res = requests.get(url,headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    #헤드라인 뉴스 3건
    print("[헤드라인 뉴스]\n")
    hdline_article_lst = soup.find("ul", attrs = {"class" : "hdline_article_list"})
    articles = hdline_article_lst.find_all("div", attrs = {"class", "hdline_article_tit"})

    for idx, article in enumerate(articles):
        link = "https://news.naver.com"+ article.a["href"]
    
        title = article.a.get_text().strip()

        print(idx+1,".",title)
        print("\t(링크 : {}".format(link))

    print("-"*20)
   #IT뉴스 3건
    print("[IT/과학 뉴스]\n")
    it_articles = soup.find("ul", attrs = {"class" : "mlist2 no_bg"}).find_all("li")
    for idx, article in enumerate(it_articles):
        link = article.a["href"]
        title = article.strong.get_text().strip()

        print(f"{idx+1}. {title}")
        print(f"\t{link}")

 

def hackers_daily_english(today_number):
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&uid={}".format(today_number)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    #해커스 어학원 오늘의 영어 회화 지문
    print("[오늘의 영어 회화]\n")# 오늘 날짜도 제시하면 좋을 듯

    conv_boxes = soup.find_all("div", attrs = {"class" : "conv_txtBox"}) #한국 및 영어 회화 box
    language = ["(한글 지문)" , "(English script)"]

    for idx, conv_box in enumerate(conv_boxes):
        conv_title = conv_box.find("b", attrs ={"class": "conv_txtTitle"}).get_text()
        lines = conv_box.find_all("span", attrs = {"class" : "conv_sub"})

        print(f"{language[idx]}-{conv_title}\n")

        for line in lines:
            line = line.get_text()
            print(line)

        print("")
        

## 위치 정보(str) : "09290125"(성북구 안암동5가), "11185106"(연수구 송도동), "09290610"(보문동)
today_weather("09290125")
print("="*100)
news()
print("="*100)
hackers_daily_english("5281") #21.5.20 : 5281




#2. 헤드라인 뉴스 3건

#3. IT 뉴스 3건

#4. 해커스 어학원 오늘의 영어 회화 지문