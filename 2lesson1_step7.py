from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

    # Ваш код, который заполняет обязательные поля
	x_element = browser.find_element_by_css_selector("#treasure").get_attribute("valuex")
	x = x_element
	y = calc(x)
	
	browser.find_element_by_css_selector("#answer").send_keys(y)
	
	browser.find_element_by_css_selector("#robotCheckbox").click()
	browser.find_element_by_css_selector("#robotsRule").click()

    # Отправляем заполненную форму
	button = browser.find_element_by_css_selector("[type=submit]")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()