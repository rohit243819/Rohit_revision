from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import time

serv_obj=Service("C:\DRIVERS\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()


driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

alert_window=driver.switch_to.alert

alert_window.send_keys("Rohit Adhav")
print(alert_window.text)

# alert_window.accept()          ## accept alert window with variable

# or alert window using cancel button

alert_window.dismiss()