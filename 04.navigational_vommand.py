import time

from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get(("https://opensource-demo.orangehrmlive.com/"))

driver.get(("https://www.nopcommerce.com/en"))

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()

time.sleep(3)


driver.close()