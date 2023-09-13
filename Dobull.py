import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://testautomationpractice.blogspot.com/")
drivers.execute_script("window.scrollBy(0,600)","")
element=drivers.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
Act=ActionChains(drivers)
Act.double_click(element).perform()
time.sleep(6)