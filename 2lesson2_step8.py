from selenium import webdriver
import time
import os

#Задание: загрузка файла

try: 
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_css_selector("[name=firstname]")
	input1.send_keys("Ivan")
	input2 = browser.find_element_by_css_selector("[name=lastname]")
	input2.send_keys("Petrov")
	input3 = browser.find_element_by_css_selector("[name=email]")
	input3.send_keys("chelovek@yaya.ruru")
	
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')
	browser.find_element_by_css_selector("#file").send_keys(file_path)
	
    # Отправляем заполненную форму
	button = browser.find_element_by_css_selector("[type=submit]")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()