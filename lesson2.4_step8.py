from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

url = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome('./chromedriver')
    browser.get(url)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id("book").click()
    browser.execute_script("window.scrollBy(0, 200);")
    x = int(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(x)))))
    browser.find_element_by_id("solve").click()
    
finally:
    print(browser.switch_to.alert.text)
    browser.quit()
    pass