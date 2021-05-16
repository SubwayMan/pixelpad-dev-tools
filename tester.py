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

options = webdriver.ChromeOptions()
options.add_argument("headless")

PATH = "C:\Program Files (x86)\chromedriver.exe" 
#driver = webdriver.Chrome(PATH, chrome_options=options)
driver = webdriver.Chrome(PATH)

def get_element(by_type, flag):
    try:
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by_type, flag)))

    except:
        raise
    
driver.get("https://pixelpad.io")

try:
    elem = get_element(By.ID, "pixelpad_login")
    elem.click()
    emailfield = get_element(By.ID, "login_username")
    passfield = get_element(By.ID, "login_password")
    emailfield.send_keys(auth.name)
    passfield.send_keys(auth.pwd)
    passfield.send_keys(Keys.RETURN)

#    driver.find_element_by_xpath('//a[contains(@href,"href")]')
    myappbut = get_element(By.LINK_TEXT, "MY PAD")
    myappbut.click()
    
    app = get_element(By.CLASS_NAME, "\"col-12 col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-4 pr-3\"")
#    app = driver.find_element_by_class_name("col-12 col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-4 pr-3")
    app.click()

except:
    driver.close()
    raise

