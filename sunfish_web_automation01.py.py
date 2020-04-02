# 200331 18:09
# 200401 14:14
# 200402 11:47

# 네이버 자동 로그인
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
# driver.find_elements_by_id("id").send_keys("아무거나")
# driver.find_elements_by_id("pw").send_keys("아무거나")
# 왜 s 붙였냐ㅋㅋ

driver.find_element_by_id("id").send_keys("id")
driver.find_element_by_id("pw").send_keys("password")
driver.find_element_by_id("log.login").click()