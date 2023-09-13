from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
drivers=webdriver.Chrome(executable_path=r"C:\Users\ram\Desktop\Drivers\chromedriver.exe")
drivers.maximize_window()
drivers.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
data=drivers.get_cookies()
print(len(data))
print(data)
add={
"name":"Ramudu",
"value":"0123456789"
}
drivers.add_cookie(add)
data1=drivers.get_cookies()
print(len(data1))
print(data1)
drivers.delete_all_cookies()
add={
"name":"Ramudu",
"value":"0123456789"
}
drivers.add_cookie(add)
data1=drivers.get_cookies()
print(len(data1))
print(data1)