from selenium import webdriver
import math


url = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome("./chromedriver")
    browser.get(url)
    browser.find_element_by_class_name("trollface.btn.btn-primary").click()
    browser.switch_to.window(browser.window_handles[-1])
    x = int(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(x)))))
    browser.find_element_by_class_name("btn.btn-primary").click()
finally:
    print(browser.switch_to.alert.text)
    browser.quit()