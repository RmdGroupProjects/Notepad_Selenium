import time
import Xuntill
path=r"C:\Users\ram\Desktop\OrangeHrm.xlsx"
rows=Xuntill.getrowCount(path,"Sheet1")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

for i in range(2,rows+1):
    username=Xuntill.redrowdata(path,"Sheet1",i,1)
    password=Xuntill.redrowdata(path,"Sheet1",i,2)
    drivers.implicitly_wait(6)
    drivers.find_element(By.NAME,"username").send_keys(username)
    drivers.find_element(By.NAME,"password").send_keys(password)
    drivers.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    #drivers.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
    #drivers.find_element(By.LINK_TEXT,"Logout").click()
    if drivers.title =="OrangeHRM":
        print("Test Passwed")
        Xuntill.writedata(path,"Sheet1",i,3,"Test Pass")
    else:
        print("Test Failed")
        Xuntill.writedata(path,"Sheet1",i,3,"Test Failed") 
    time.sleep(6)