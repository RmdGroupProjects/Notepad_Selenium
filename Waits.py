import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#time.sleep(6)
drivers.implicitly_wait(6)
drivers.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(6)
drivers.find_element(By.NAME,"password").send_keys("admin123")
drivers.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
time.sleep(6)
