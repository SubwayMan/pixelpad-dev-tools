import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

try:
    import auth

except ModuleNotFoundError:

    print("Login details missing. Setting up auth...")
    usern = input("Enter name: ")
    userp = input("Enter password: ")
    autoname = input("Enter a name for the temporary apps. If you have any existing apps with this name, they will be deleted.")
    au = open("auth.py", "w")
    out = "name = \"" + usern + "\"\npwd = \"" + userp + "\"\nautoname = \"" + autoname + "\""
    au.write(out)
    au.close()
    import auth

options = webdriver.ChromeOptions()
options.add_argument("headless")
PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH, chrome_options=options)
#driver = webdriver.Chrome(PATH)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

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

    myappbut = get_element(By.LINK_TEXT, "MY PAD")
    myappbut.click()
    makeappbut = get_element(By.ID, "create_a_new_app_button")
    makeappbut.click()
    namefield = get_element(By.ID, "appcreate_name")
    namefield.send_keys(auth.autoname)
    confbut = get_element(By.ID, "create_app_confirm_button")
    confbut.click()

    close_docs = get_element(By.LINK_TEXT, "Close")
    close_docs.click()
    driver.find_element_by_xpath("//div[@id='pixelpad_nav_topbar']/div[1]/div[1]").click()
    driver.find_element_by_link_text("IMPORT").click() 

    fileinp = driver.find_element_by_id("importProject")
    fileinp.send_keys(os.path.join(os.getcwd(), "inp.pp2d"))
    driver.implicitly_wait(2)
    driver.find_element_by_id("importProjectButton").click()

    driver.switch_to.alert.accept()
    try:
        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//div[@id='importModal']/div[1]/div[1]/div[2]/button[1]").click()

    except selenium.common.exceptions.NoSuchElementException:
        pass
    
    print("Running pixelpad file...")
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID, "pp-start"))).click()
    time.sleep(2)

    outfile = open("out.txt", "w")
    cont = driver.find_element_by_id("output").text
    outfile.write(cont)
    outfile.close()
    print("PixelPad file successfully ran. Output logged.")
    print("Cleaning up now...")
    driver.back()
    driver.back()
    driver.implicitly_wait(10)


    lastapp = driver.find_element_by_xpath("//div[@class='col-12 col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-4 pr-3']")          

    dropd = lastapp.find_element_by_id("dropdownMenuButton")
    actions.move_to_element(dropd).perform()
    dropd.click()
    editbut = lastapp.find_element_by_xpath("//a[@class='dropdown-item edit-project']")
    actions.move_to_element(editbut).perform()
    editbut.click()

    driver.find_element_by_id("confirm_delete_button").click()
    driver.find_element_by_id("pixelpad_shift_delete").click()
    time.sleep(5)

    print("Program successfully terminated.")
    driver.close()

except:
    driver.close()
    raise

