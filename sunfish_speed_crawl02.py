# 네이트판 여러 페이지 크롤링하기

import requests
from bs4 import BeautifulSoup

for i in range(0, 11):
    # 엔터치기
    req = requests.get("https://pann.nate.com/talk/c20002?page=" + str(i))

    # 이런 식으로 HTML에 있는 코드를 다 가져온다.
    soup = BeautifulSoup(req.text, 'html.parser')

    for i in soup.select("#searchDiv > div.posting_wrap > table > tbody > tr"):
        print(i.find("a").text)
