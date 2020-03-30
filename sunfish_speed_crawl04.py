# url로 크롤링 하기

import requests
from bs4 import BeautifulSoup

# 엔터치기
req = requests.get("http://www.donga.com/news/List/Enter/?p=1&prod=news&ymd=&m=")

# html 받아오기
soup = BeautifulSoup(req.text, 'html.parser')

for i in soup.find_all("div", class_="rightList"):
    print()

    req_new = requests.get(i.find("a")["href"])

    soup_new = BeautifulSoup(req_new.text, "html.parser")

    print(soup_new)

