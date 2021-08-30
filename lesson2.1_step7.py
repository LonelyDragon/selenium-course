from selenium import webdriver
import time
import math


url = "http://suninjuly.github.io/get_attribute.html"

def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    x = browser.find_element_by_id("treasure").get_attribute("valuex")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))
    robo_check = ['//input[@value="robots"]', '//input[@id="robotCheckbox"]']
    for selector in robo_check:    
        browser.find_element_by_xpath(selector).click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
