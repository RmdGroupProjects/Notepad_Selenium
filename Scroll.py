import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://www.nationsonline.org/oneworld/countries_of_the_world.htm")
#drivers.execute_script("window.scrollBy(0,1200)","")
#drivers.execute_script("window.scrollBy(0,document.body.scrollHeight)")
drivers.implicitly_wait(6)
element=drivers.find_element(By.XPATH,"/html/body/div[7]/div/table[3]/tbody/tr[11]/td[2]/a]") # Pending
drivers.execute_script("argument[0].scrollIntoView(),",element)
time.sleep(6)