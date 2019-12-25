from selenium import webdriver
import time
import math

#Задание: принимаем alert

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	browser.find_element_by_css_selector("[type=submit]").click()
	alert = browser.switch_to.alert
	alert.accept()
	
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	y = calc(x)
	
	answer = browser.find_element_by_css_selector("#answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
	answer.send_keys(y)
	
    # Отправляем заполненную форму
	button = browser.find_element_by_css_selector("[type=submit]")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()