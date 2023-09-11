import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://demo.automationtesting.in/Windows.html")
print(drivers.current_window_handle)
time.sleep(6)
handles=drivers.window_handles
for i in handles:
    drivers.switch_to.window(i)
    print(drivers.title)