import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(drivers.title)
time.sleep(6)
drivers.get("https://www.facebook.com/login.php/")
print(drivers.title)
time.sleep(6)
drivers.back()
print(drivers.title)
time.sleep(6)
drivers.forward()
print(drivers.title)
