from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)

    # Ваш код, который заполняет обязательные поля
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	y = calc(x)
	
	browser.find_element_by_css_selector("#answer").send_keys(y)
	
	browser.find_element_by_css_selector("[for=robotCheckbox]").click()
	browser.find_element_by_css_selector("[for=robotsRule]").click()

    # Отправляем заполненную форму
	button = browser.find_element_by_css_selector("[type=Submit]")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()