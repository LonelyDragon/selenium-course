from selenium import webdriver
import time
import math
url = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome("./chromedriver")
    browser.get(url)
    browser.find_element_by_class_name("btn.btn-primary").click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element_by_id("input_value").text)
    #What is ln(abs(12*sin(x))), where x = 389?
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(x)))))
    browser.find_element_by_class_name("btn.btn-primary").click()
finally:
    print(browser.switch_to.alert.text)
    browser.quit()