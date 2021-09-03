from posixpath import join
from selenium import webdriver
import time
import os


url = "http://suninjuly.github.io/file_input.html"
folder_path = os.path.abspath(os.path.dirname(__file__))
file_name = "simple.txt"
file_path = os.path.join(folder_path, file_name)
with open(file_name, "w+") as f:
    f.close()

try:
    browser = webdriver.Chrome('./chromedriver')
    browser.get(url)
    browser.find_element_by_name("firstname").send_keys("Anton")
    browser.find_element_by_name("lastname").send_keys("Zavodchikov")
    browser.find_element_by_name("email").send_keys("abc@mail.ru")
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
    os.remove(file_name)