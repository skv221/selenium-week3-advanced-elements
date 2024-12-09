from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website which uses hoverable dropdowns
url = "https://www.iwmf.org/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

actions = ActionChains(driver)

#Select Opportunities from dropdown menu through hovering and navigate until kim wall memorial fund
menu = driver.find_element(By.XPATH, "//a[@href='https://www.iwmf.org/our-programs/']")
actions.move_to_element(menu).perform()
time.sleep(5)

subMenu = driver.find_element(By.XPATH, "//a[text()='Grants & Funds']")
actions.move_to_element(subMenu).perform()
time.sleep(5)

subMenu2 = driver.find_element(By.XPATH, "//a[@href='/programs/kim-wall-memorial-fund/']")
actions.move_to_element(subMenu2).perform()
time.sleep(3)
subMenu2.click()

driver.implicitly_wait(5)

#validate whether desired operation is done
if driver.find_element(By.XPATH, "//div[@class='text']/h1[text()='Kim Wall Memorial Fund']"):
    print("Task done successfully!!")
else:
    print("Something went wrong!!")


time.sleep(5)
driver.quit()