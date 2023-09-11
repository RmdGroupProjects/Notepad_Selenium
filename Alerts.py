import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://testautomationpractice.blogspot.com/")
drivers.implicitly_wait(6)
drivers.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button[1]").click()
time.sleep(6)
drivers.switch_to_alert().accept()
time.sleep(6)