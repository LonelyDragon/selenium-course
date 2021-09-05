from selenium import webdriver
import unittest


def url_test(url) -> str:

    browser = webdriver.Chrome("./chromedriver")
    browser.get(url)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    last_name = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    email = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')

    fields = [first_name, last_name, email]
    # Отправляем заполненную форму
    for field in fields:
        field.send_keys("test")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    # time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

    browser.quit()
    return welcome_text

class Test(unittest.TestCase):

    def test_reg1(self):
        self.assertEqual(url_test("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!")

    def test_reg2(self):
        self.assertEqual(url_test("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!")

if __name__ == '__main__':
    unittest.main()