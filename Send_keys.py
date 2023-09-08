import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://www.facebook.com/login.php/")
drivers.find_element(By.ID,"email").send_keys("uramudu257@gmail.com")
drivers.find_element(By.ID,"pass").send_keys("Ramudu123@")
drivers.find_element(By.NAME,"login").click()
time.sleep(6)