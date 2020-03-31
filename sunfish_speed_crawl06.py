# 200331 10:02
# 셀레니움 활용

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
# 3초 쉬고
driver.implicitly_wait(3)
# url에 접근
driver.get('http://www.todayhumor.co.kr/')
# HTML형태로 받아와서 soup에 넣어놓음
# 오늘의 유머 사이트로 접속해서 나오는 제목들을 다 크롤링 한 다음
soup = BeautifulSoup(driver.page_source, 'html.parser')

for i in soup.find_all("td", class_="subject") :
    print(i.text)

# 그 다음 베스트오브베스트 라는 버튼을 눌러서, 나오는 게시글들의 제목을 크롤링
driver.find_element_by_id("span_topmenu_bestofbest").click()

print("구분선 --- ------")

soup = BeautifulSoup(driver.page_source, 'html.parser')

for i in soup.find_all("td", class_="subject") :
    print(i.text)

# 자유게시판 제목 크롤링
print("구분선2 --- ------")
driver.find_element_by_id("span_topmenu_freeboard").click()

for i in soup.find_all("td", class_="subject") :
    print(i.text)

print("구분선3 --- ------")

# driver.close()