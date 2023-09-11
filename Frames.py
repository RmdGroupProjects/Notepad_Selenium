import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://www.google.co.in/")
time.sleep(6)
drivers.find_element(By.XPATH,"//*[@id='gbwa']/div/a").click()
time.sleep(6)
drivers.switch_to.frame("app")
drivers.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/ul/li[5]/a/div/span").click()
time.sleep(6)