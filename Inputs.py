import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
drivers.find_element(By.ID,"RESULT_TextField-1").send_keys("Ramudu")
drivers.find_element(By.ID,"RESULT_TextField-2").send_keys("Uppari")
drivers.find_element(By.ID,"RESULT_TextField-3").send_keys("1234567891")
drivers.find_element(By.ID,"RESULT_TextField-4").send_keys("India")
drivers.find_element(By.ID,"RESULT_TextField-5").send_keys("Nandyal")
drivers.find_element(By.ID,"RESULT_TextField-6").send_keys("Ramudu@gmail.com")
time.sleep(6)