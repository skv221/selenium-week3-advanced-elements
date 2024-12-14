from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website \
url = "https://www.tutorialspoint.com/selenium/practice/frames.php"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

actions = ActionChains(driver)

#Selecting the iframes
iframe_1 = driver.find_element(By.XPATH, "//div[@class='col-md-8 col-lg-8 col-xl-8']/iframe[1]")
iframe_2 = driver.find_element(By.XPATH, "//div[@class='col-md-8 col-lg-8 col-xl-8']/iframe[2]")

#Switching to iframe 1
driver.switch_to.frame(iframe_1)
print("Switched to iframe 1.... Printing the title...")
time.sleep(5)
title = driver.find_element(By.XPATH, "//h1[text()='Selenium - Automation Practice Form']")
print(title.text)

#switching to main content
driver.switch_to.default_content()

#Switching to iframe 2
driver.switch_to.frame(iframe_2)
print("Switched to iframe 2.... Clicking the link to Selenium tutorial...")
time.sleep(5)
link = driver.find_element(By.XPATH, "//header[@class='header selenium bg-white p-3 ']/div[3]/a")
actions.move_to_element(link).click().perform()
print("Navigated to Selenium tutorial")
time.sleep(5)

driver.quit()