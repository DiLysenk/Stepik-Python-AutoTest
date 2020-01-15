from selenium import webdriver
import time
import unittest


class TestStepik(unittest.TestCase):
    def test_TestCase1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")

        input_lustname = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input_lustname.send_keys("lys")

        input2 = browser.find_element_by_css_selector(".form-control.third")
        input2.send_keys("dilys@g.com")

        input3 = browser.find_element_by_css_selector("[placeholder='Input your phone:']")
        input3.send_keys("9996699")

        input4 = browser.find_element_by_css_selector("[placeholder='Input your address:']")
        input4.send_keys("SPB")

        time.sleep(1)

        sumbit = browser.find_element_by_css_selector(".btn.btn-default")
        sumbit.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        time.sleep(1)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_TestCase2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")

        input_lustname = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input_lustname.send_keys("lys")

        input2 = browser.find_element_by_css_selector(".form-control.third")
        input2.send_keys("dilys@g.com")

        input3 = browser.find_element_by_css_selector("[placeholder='Input your phone:']")
        input3.send_keys("9996699")

        input4 = browser.find_element_by_css_selector("[placeholder='Input your address:']")
        input4.send_keys("SPB")

        time.sleep(1)

        sumbit = browser.find_element_by_css_selector(".btn.btn-default")
        sumbit.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        time.sleep(1)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()






