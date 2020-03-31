# 200331 13:37
# 실전 크롤링 BeautifulSoup

import requests
from bs4 import BeautifulSoup

req = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=펭수")

soup = BeautifulSoup(req.text, 'html.parser')

for i in soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li") :
    print(i.find("dt").text)

url_list = []
for j in soup.select("#main_pack > div > div.paging > a") :
    url_list.append("https://search.naver.com/search.naver" + j["href"])

for k in range(0,5) :
    print("------")
    req2 = requests.get(url_list[k])

    soup2 = BeautifulSoup(req2.text, 'html.parser')

    for l in soup2.select("#main_pack > div.news.mynews.section._prs_nws > ul > li"):
        print(l.find("dt").text)