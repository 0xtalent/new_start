# url로 크롤링 하기

import requests
from bs4 import BeautifulSoup

for i in range(0, 11):
    # 엔터치기
    req = requests.get("http://www.donga.com/news/List/Enter/?p=1&prod=news&ymd=&m=")

    # html 받아오기
    soup = BeautifulSoup(req.text, 'html.parser')

    for i in soup.select("#contents > div.page > a"):

        req2 = requests.get("http://www.donga.com/news/List/Enter/" + i['href'])

        soup2 = BeautifulSoup(req2.text, "html.parser")

        for i  in soup2.find_all("span", class_="tit"):
            print(i.text)
