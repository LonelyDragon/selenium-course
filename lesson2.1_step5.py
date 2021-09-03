from selenium import webdriver
import time
import math


url = "http://suninjuly.github.io/math.html"

def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome("./chromedriver")
    browser.get(url)
    x = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x.text))
    robo_check = ['//label[@for="robotsRule"]', '//label[@for="robotCheckbox"]']
    for selector in robo_check:    
        browser.find_element_by_xpath(selector).click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()