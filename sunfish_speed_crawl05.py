from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
# 3초 쉬고
driver.implicitly_wait(3)
# url에 접근
driver.get("http://www.google.com")