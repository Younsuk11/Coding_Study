# pip install requests  : module 설치
# Requests library: web scrapping  = web page의 문서 정보 가져오기

import requests
res = requests.get("http://goolge.com")

# 실제로 가져올수 있는지 여부를 확인
# print("응답 코드 : ", res.status_code) # 200이면 정상

# res1 = requests.get("http://nadocoding.tistory.com")

# print("응답코드 : ", res1.status_code) ## 403 이면 비정상 (권한이 없음.)


## 정상여부 확인 작업
# if res.status_code == requests.codes.ok : 
#     print("정상입니다.")

# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code,"]")

## 정상 여부 확인 작업(2)
res.raise_for_status()  ## 비정상(403)이면 error출력, 프로그램 종료
# print("웹 스크래핑을 진행합니다.")



# ##따라서 : 기본 문장들....
# import requests
# res = requests.get("http://naver.com")
# res.raise_for_status()

print(len(res.text)) # html의 문자 개수
print(res.text)

#html내용 파일로 저장 .html형식으로
with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)