from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import time

serv_obj=Service("C:\DRIVERS\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

#select specipic box

# driver.find_element(By.XPATH,'//*[@id="monday"]').click()

# to select all checkbox
checkboxes1 = driver.find_elements(By.XPATH,'//input[@type="checkbox" and contains(@id,"day")]')
print(len(checkboxes1))

#approach1
for i in range(len(checkboxes1)):
    checkboxes1[i].click()

'''
#approach2
for checkbox in checkboxes1:
    checkbox.click()

#approach3
#select multiple checkboxes by choice:

for checkbox in checkboxes1:
    weekname=checkbox.get_attribute("id")
    if weekname== 'monday' or weekname=='sunday':
        checkbox.click()


#approach(select last 2checkboxes)

for i in range(len(checkboxes1)-2,len(checkboxes1)):
    checkboxes1[i].click()


#approach(select first 2checkboxes)

for i in range(len(checkboxes1)):
    if i<2:           #for first 3 checkboxes:i<2:
        checkboxes1[i].click()
'''

time.sleep(5)
#approach6 (how to clear all checkboxes)

for checkbox in checkboxes1:
    if checkbox.is_selected():
        checkbox.click()