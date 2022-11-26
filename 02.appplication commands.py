

from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get(("https://opensource-demo.orangehrmlive.com/"))

abc=driver.current_url
print(abc)


a=123
b=234
print(a,b)

driver.close()