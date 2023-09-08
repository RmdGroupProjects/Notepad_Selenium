from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
title=drivers.title
print(title)
url=drivers.current_url
print(url)
drivers.close()

