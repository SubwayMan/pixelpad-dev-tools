from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
	import auth

except ModuleNotFoundError:

	print("Login details missing. Setting up auth...")
	usern = input("Enter name: ")
	userp = input("Enter password: ")

	au = open("auth.py", "w")
	out = "name = \"" + usern + "\"\npwd = \"" + userp + "\""
	au.write(out)
	au.close()
	import auth

PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH)
driver.get("https://pixelpad.io/wp-login.php")

emailfield = driver.find_element_by_name("log")
passfield = driver.find_element_by_name("pwd")
emailfield.send_keys(auth.name)
passfield.send_keys(auth.pw)

passfield.send_keys(Keys.RETURN)


