from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\DRIVERS\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()


# drpcountry_ele=driver.find_element(By.XPATH,'//*[@id="input-country"]')
# drpcountry=select(drpcountry_ele)

drpcountry=Select(driver.find_element(By.XPATH,'//select[@id="input-country"]'))


#select options from the drop down:
drpcountry.select_by_visible_text("India")


###########    OR      #######

drpcountry.select_by_value("13")

# or
drpcountry.select_by_index(13)

#capture all number of options and print them

alloptions=drpcountry.options
print("total options are:",  len(alloptions))

#to print all options name

for opt in alloptions:
    print(opt.text)

#select option from dropdown without using built in functions:

# for opt in alloptions:
#     if opt.text=="India":
#         opt.click()
#         break

for opt in alloptions:
    if opt.text=="India":
        opt.click()
        break


a=123
b=234
print(a,b)