import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.get("https://testautomationpractice.blogspot.com/")
e1=drivers.find_element(By.ID,"draggable")
e2=drivers.find_element(By.ID,"droppable")
Act=ActionChains(drivers)
Act.drag_and_drop(e1,e2).perform()
time.sleep(6)
