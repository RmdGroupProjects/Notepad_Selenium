import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
drivers.implicitly_wait(6)
drivers.find_element(By.XPATH,"//*[@id='q26']/table/tbody/tr[1]/td").is_enabled()
drivers.find_element(By.XPATH,"//*[@id='q26']/table/tbody/tr[1]/td").click()
time.sleep(6)