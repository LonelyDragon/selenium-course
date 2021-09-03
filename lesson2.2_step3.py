from selenium import webdriver
import time


url = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome('./chromedriver')
    browser.get(url)
    value1 = int(browser.find_element_by_id('num1').text)
    value2 = int(browser.find_element_by_id('num2').text)
    browser.find_element_by_class_name("custom-select").click()
    browser.find_element_by_css_selector(f"[value='{int(value1)+int(value2)}']").click()
    browser.find_element_by_class_name("btn.btn-default").click()
finally:
    time.sleep(10)
    browser.quit()
