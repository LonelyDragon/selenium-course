from selenium import webdriver
import pytest
import math
import time


urls = [
    "236895",
    "236896",
    "236897",
    "236898",
    "236899",
    "236903",
    "236904",
    "236905"
]
sol = ""


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("./chromedriver")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', urls)
def test_input(browser, url):
    browser.get(f"https://stepik.org/lesson/{url}/step/1")
    browser.implicitly_wait(5)
    browser.find_element_by_tag_name("textarea").send_keys(
        str(math.log(int(time.time()))))
    browser.find_element_by_class_name("submit-submission").click()
    answer = browser.find_element_by_class_name("smart-hints__hint").text
    assert answer == 'Correct!'