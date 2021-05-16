from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import auth

PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH)
driver.get("https://pixelpad.io/wp-login.php")

emailfield = driver.find_element_by_name("log")
passfield = driver.find_element_by_name("pwd")
emailfield.send_keys(auth.name)
passfield.send_keys(auth.pw)

passfield.send_keys(Keys.RETURN)


