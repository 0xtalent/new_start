# 200331 17:13

from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.google.com/search?q=%ED%8E%AD%EC%88%98&source=lnms&tbm=isch&sa")

for i in range(1,5) :

    scroll_index = i * 1000
    # 1000, 2000, 3000, 4000

    driver.execute_script("window.scrollTo(0," + str(scroll_index) + ")")

    time.sleep(3)

    driver.get_screenshot_as_file("data/test" + str(scroll_index) + ".png")