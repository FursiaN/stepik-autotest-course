from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link= "http://suninjuly.github.io/get_attribute.html"
try:
    browser=webdriver.Chrome()
    browser.get(link)
    xValue=browser.find_element_by_id('treasure')
    x=xValue.get_attribute('valuex')
    y=calc(x)
    textarea=browser.find_element_by_id('answer')
    textarea.send_keys(y)
    checkbox1=browser.find_element_by_id('robotCheckbox')
    checkbox1.click()
    radio1=browser.find_element_by_id('robotsRule')
    radio1.click()
    button=browser.find_element_by_tag_name('button')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()