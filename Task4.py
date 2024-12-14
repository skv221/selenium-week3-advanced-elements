from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website 
url = "https://www.tutorialspoint.com/selenium/practice/browser-windows.php"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

main_window = driver.current_window_handle

#Select button to open in new tab
newTab = driver.find_element(By.XPATH, "//button[@title='New Tab']")
time.sleep(5)
newTab.click()

print("Switching to new Tab... Printing the heading...")
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

newTabTitle = driver.find_element(By.XPATH, "//h1[@class='mb-3 fw-normal border-bottom text-left pb-2 mb-4']")
print(newTabTitle.text)
driver.close()

print("Switching back to main window...")
driver.switch_to.window(main_window)

#Select button to open in new window
newWindow = driver.find_element(By.XPATH, "//button[text()='New Window Message']")
time.sleep(5)
newWindow.click()

print("Switching to new window... Printing the message in new window...")
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

newWindowMessage = driver.find_element(By.XPATH, "//div[@class='row d-flex justify-content-center logindiv bg-white rounded']")
print(newWindowMessage.text)
driver.close()

print("Switching back to main window... Exiting...")
driver.switch_to.window(main_window)
time.sleep(5)
driver.quit()
