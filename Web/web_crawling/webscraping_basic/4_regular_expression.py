# regular expression : 해당 내용에 대한 정해진 형식(specification)

# ex) 주민번호 : 6자리 - 7자리  / 이메일 : email@naver.com

import re

# 교통사고 목격 , 뺑소니, 차번호판
# ca?e
# cafe, case, cave, care.........
# caae, cabe, cace,cade.......
# regular expression

p = re.compile("ca.e") # pattern 지정
#(ca.e) . : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
#(^de) ^ : 문자열의 시작 > desk, destination(o) | fade(x)
# (se$) $ : 문자열의 끝 > case , base | face(x)


def print_match(m):
    if m : 
        print("m.group() : ", m.group())
        
        #group() : 기준(ca.e) 매칭된다면 일치한 문자열만 ex) ca.e - care 매칭 가능 : care값 저장
        #기준에 부합하지 않으면(m = p.search("good care")에서 매칭된 내용 없음) error 발생
    
        print("m.string : ",m.string) # 일치한다면, 입력받은 문자열 전체( string = 함수x, 변수임.)
        print("m.start(): ", m.start()) # 일치하는 입력받은 문자열의 시작 index
        print("m.end() : ", m.end()) # 일치하는 입력받은 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 입력받은 문자열의 시작  /  끝 index

    else:
        print("매칭되지 않았습니다.") # 여부에 따라 error되지 않고, 계속 진행.



# m = p.match("good care") # 받은 input값과 p가 matching하는지 여부 정보(type: re.Match)
# # 경우들
# #"good care" : 앞 부분에 추가적으로 받기 때문에 match x
# #"careless" : ca.e(less) match 가능 / match : 주어진 문자열의 처음부터 일치하는지 확인.


# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인

# print_match(m) # output = care

#[경우] : good care , careless
#group() 결과
#"good care" : ca.e 과 일치하는 단어가 있으므로 care 출력
#"careless" : 역시 ca.e(기준)과 매칭되는 care가 문자열 중에 있으므로 care grouping

#m.string 결과
#"good care" : good care

#m.start()  : 5
#m.end(): 9
#m.span() : (5,9)



lst = p.findall("careless cafe")  # findall : 일치하는 모든 것을 리스트 형태로 반환 ( 즉 여러개가 일치한다면 모두 리스트 형태로 반환)
print(lst)#['care', 'cafe']



#############################################

# 1. p= re.compile("원하는 정규식,형태")
# 2. m = p.match("비교할 문자열") : 처음부터 일치하는지 일치 확인
# 3. m = p.search("비교할 문자열") : 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트"형태로 반환

# 원하는 형태 : 정규식
# #(ca.e) . : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# (^de) ^ : 문자열의 시작 > desk, destination(o) | fade(x)
# (se$) $ : 문자열의 끝 > case , base | face(x)


# # 정규식 공부 : w3schools.com > learn python > RegEX or python re(docs.python.org - 공식 홈페이지)


