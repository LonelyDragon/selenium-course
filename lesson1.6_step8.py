from selenium import webdriver
import time 

url = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    for element in browser.find_elements_by_tag_name("input"):
        element.send_keys("test")
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
finally:
    time.sleep(15)
    browser.quit()