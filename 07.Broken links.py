# we need to install requests package --> setting> interpreter --> Rquets --> install package

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests


serv_obj=Service("C:\DRIVERS\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks=driver.find_elements(By.TAG_NAME,'a')
count=0

for link in allLinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url,"   is broken link")
        count+=1

    else:
        print(url,"   is valid link")

print("Total no of broken links:",count)


driver.close()