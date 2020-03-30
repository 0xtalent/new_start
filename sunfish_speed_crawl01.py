# 네이트판 크롤링

import requests
from bs4 import BeautifulSoup

# 엔터치기
req = requests.get("https://pann.nate.com/talk/c20002?page=1")

# 이런 식으로 HTML에 있는 코드를 다 가져온다.
soup = BeautifulSoup(req.text, 'html.parser')

for i in soup.select("#searchDiv > div.posting_wrap > table > tbody > tr"):
    print(i.find("a").text)
