# User Agent

# 해당 웹사이트를 접속하는 사용자(사람, mobile)에 따라 맞는 웹 사이트를 제공한다.
# but 프로그램이 접속하는 경우, 웹사이트 자체가 차단할 수 있음.
# 이때, User agent를 통해서 처리 할 수 있음.

# [웹 스크래핑 변경사항]
# 1. "티스토리"는 UserAgent 를 변경하지 않아도 정상적으로 html 을 받아옵니다.

# My user agent (현 시점 나의 user agent)
# : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36

import requests

url = "http://nadocoding.tistory.com"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

res = requests.get(url, headers = headers) ## requests를 할 때, 접속하는 해당 user agent값을 넘겨줌.
res.raise_for_status()

with open("nadocoding.html", "w", encoding = "utf8") as f:
    f.write(res.text)