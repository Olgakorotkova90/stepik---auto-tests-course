from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)
num1=browser.find_element_by_id('num1').text
num2=browser.find_element_by_id('num2').text
sum=int(num1)+int(num2)

select1 = Select(browser.find_element_by_tag_name("select"))

select1.select_by_value(str(sum))

button = browser.find_element_by_css_selector('[type= "submit"]')
button.click()

