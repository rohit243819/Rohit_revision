from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\DRIVERS\chrome_driver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()


# click on link
driver.find_element(By.LINK_TEXT,"Digital downloads").click()


a=123
b=234
print(a,b)

# #find number of links on page:
# links=driver.find_elements(By.TAG_NAME,"a")
# print("total no of links:",len(links))

#               OR

# links = driver.find_elements(By.XPATH, "//a")
# print("total no of links:", len(links))

# print all links name
#
# for link in links:
#     print(link.text)

