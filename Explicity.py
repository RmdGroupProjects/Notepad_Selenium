import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(6)
drivers.find_element(By.NAME,"username").send_keys("Admin")
drivers.find_element(By.NAME,"password").send_keys("admin123")
waits=WebDriverWait(drivers,6)
elements=waits.until(Ec.element_to_be_clickable(drivers.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
elements.click()
time.sleep(6)
# https://selenium-python.readthedocs.io/waits.html