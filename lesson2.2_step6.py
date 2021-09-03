from selenium import webdriver
import time
import math


url = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome('./chromedriver')
    browser.get(url)
    x = int(browser.find_element_by_id('input_value').text)
    #ln(abs(12*sin(x)))
    browser.find_element_by_id('answer').send_keys(f'{math.log(abs(12*math.sin(x)))}')
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()
finally:
    time.sleep(10)
    browser.quit()