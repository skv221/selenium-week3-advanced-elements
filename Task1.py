from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website
url = "https://www.fleetfeet.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

#Select Brand dropdown menu and extract the Trending Brands from that menu
brands = driver.find_element(By.XPATH, "//button[@id='nav_button-brands']")
brands.click()
trendingBrands = driver.find_elements(By.XPATH, "//div[@class='dropdown-secondary']/ul/li[2]/ul/li")

for brand in trendingBrands:
    if(brand.text != ""):
        print(brand.text)
    
time.sleep(5)
driver.quit()
