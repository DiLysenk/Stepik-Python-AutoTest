from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


button1 = browser.find_element_by_css_selector(".btn.btn-primary")
button1.click()

time.sleep(1)

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_css_selector("#input_value").text
x = int(x)

answer = math.log(abs(12 * math.sin(x)))
answer = str(answer)

answer_element = browser.find_element_by_css_selector('#answer')
answer_element.send_keys(answer)

sumbit = browser.find_element_by_css_selector(".btn.btn-primary")
sumbit.click()