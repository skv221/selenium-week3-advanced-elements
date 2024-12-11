from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website which uses clickable dropdowns
url = "https://www.tutorialspoint.com/selenium/practice/alerts.php"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

#Select and click button to trigger alert
button1 = driver.find_element(By.XPATH, "//button[@onclick='showAlert()']")
time.sleep(3)
button1.click()
time.sleep(5)

#Find and accept the alert
alert = driver.switch_to.alert
print(alert.text, "Alert exists!!")
alert.accept()

#Select and click button to trigger next alert
button2 = driver.find_element(By.XPATH, "//button[@onclick='myMessage()']")
time.sleep(3)
button2.click()

#Find and accept the alert
WebDriverWait(driver, 10).until (EC.alert_is_present())
delayedAlert = driver.switch_to.alert
time.sleep(5)
print(delayedAlert.text, "Delayed alert exists!!")
delayedAlert.accept()

#Select and click button to trigger next alert
button3 = driver.find_element(By.XPATH, "//button[@onclick='myDesk()']")
time.sleep(3)
button3.click()

#Find and accept the alert
confirmAlert = driver.switch_to.alert
time.sleep(3)
# confirmAlert.accept() -- uncomment this and comment next line for accepting the alert scenario
confirmAlert.dismiss()
message = driver.find_element(By.XPATH, "//div[@id='desk']")
print(message.text, "Confirm alert exists!!")

#Select and click button to trigger next alert
button4 = driver.find_element(By.XPATH, "//button[@onclick='myPromp()']")
time.sleep(3)
button4.click()

#Find and accept the alert
promptAlert = driver.switch_to.alert
time.sleep(3)
promptAlert.send_keys("Venkatesan S K")
print(promptAlert.text, "Prompt alert exists!!") 
promptAlert.accept()

#Here the text won't be visible in the prompt alert due to issues in chrome. It will be visible in case of firefox.
#Though it is not visible, the sent string is stored and can be retrieved if exists in DOM 
# Refer https://issues.chromium.org/issues/42320132#comment12 for more details

time.sleep(5)
driver.quit()