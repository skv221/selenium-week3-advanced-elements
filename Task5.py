from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website
url = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

actions = ActionChains(driver)

print("Performing Drag and drop operation...")
#Assigning sources and targets
source1 = driver.find_element(By.ID,'box1')
source2 = driver.find_element(By.ID,'box2')
source3 = driver.find_element(By.ID,'box3')
source4 = driver.find_element(By.ID,'box4')
source5 = driver.find_element(By.ID,'box5')
source6 = driver.find_element(By.ID,'box6')
source7 = driver.find_element(By.ID,'box7')

target1 = driver.find_element(By.ID, 'box101')
target2 = driver.find_element(By.ID, 'box102')
target3 = driver.find_element(By.ID, 'box103')
target4 = driver.find_element(By.ID, 'box104')
target5 = driver.find_element(By.ID, 'box105')
target6 = driver.find_element(By.ID, 'box106')
target7 = driver.find_element(By.ID, 'box107')

#Performing drag and drop
actions.drag_and_drop(source1,target1).perform()
time.sleep(3)
print("First drag and drop operation done")
actions.drag_and_drop(source2,target2).perform()
time.sleep(3)
print("Second drag and drop operation done")
actions.drag_and_drop(source3,target3).perform()
time.sleep(3)
print("Third drag and drop operation done")
actions.drag_and_drop(source4,target4).perform()
time.sleep(3)
print("Fourth drag and drop operation done")
actions.drag_and_drop(source5,target5).perform()
time.sleep(3)
print("Fifth drag and drop operation done")
actions.drag_and_drop(source6,target6).perform()
time.sleep(3)
print("Sixth drag and drop operation done")
actions.drag_and_drop(source7,target7).perform()
time.sleep(3)
print("Last drag and drop operation done")

driver.refresh() #Refreshing the webpage

actions = ActionChains(driver)

#Selecting and copying all text in webpage
time.sleep(5)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(3)
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(3)
driver.find_element(By.ID,'box1').click()
time.sleep(3)
print("Copied the text... Try Pasting in the CopiedTxt file or wherever you feel to paste...")

driver.quit()