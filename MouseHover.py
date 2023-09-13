import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
drivers.implicitly_wait(6)
drivers.find_element(By.NAME,"username").send_keys("Admin")
drivers.find_element(By.NAME,"password").send_keys("admin123")
waits=WebDriverWait(drivers,6)
element=waits.until(Ec.element_to_be_clickable(drivers.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
element.click()
act=ActionChains(drivers)
drivers.implicitly_wait(6)
e1=drivers.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul").click()
e2=drivers.find_element(By.LINK_TEXT,"User Management")
#e3=drivers.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a")
#act.move_to_element(e1).click().perform()
time.sleep(6)