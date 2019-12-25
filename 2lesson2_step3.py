from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x, y):
  return x+y

try: 
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

    # Ваш код, который заполняет обязательные поля
	x_element = browser.find_element_by_css_selector("#num1")
	x = x_element.text
	
	y_element = browser.find_element_by_css_selector("#num2")
	y = y_element.text
	
	z = str(calc(int(x), int(y)))
	
	browser.find_element_by_css_selector("#dropdown").click()
	
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(z)
	
    # Отправляем заполненную форму
	button = browser.find_element_by_css_selector("[type=submit]")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()