import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from datetime import datetime
import time
import os

site = sys.argv[1]

dcap = DesiredCapabilities.CHROME
dcap['goog:loggingPrefs'] = { 'browser':'ALL' }

opt = webdriver.ChromeOptions()
opt.add_argument("headless")
opt.add_argument("--ignore-certificate-errors")
opt.add_argument("--test-type")
opt.add_argument("--disable-gpu")

PATH = "/usr/bin/chromedriver" #linux
#PATH = "C:\Program Files (x86)\chromedriver.exe" #windows 10

driver = webdriver.Chrome(PATH, options=opt, desired_capabilities=dcap)
driver.get(site)

original_size = driver.get_window_size()
required_width = driver.execute_script("return document.body.parentNode.scrollWidth")
required_height = driver.execute_script("return document.body.parentNode.scrollHeight")

driver.maximize_window()
driver.set_window_size(driver.get_window_size()["width"], required_height)

dest = os.path.join(os.getcwd(), "screenshots")
if not os.path.exists(dest):
    os.mkdir(dest)

id = 1
time.sleep(5)
while True:

    fname = os.path.join(dest, "screenshot"+str(id)+".png")
    if not os.path.exists(fname):
        driver.get_screenshot_as_file(fname)
        break

    id += 1

dat = ""
if os.path.exists("debug.log"):
    dat = open("debug.log", "r").read()

print("printing console errors...")
for entry in driver.get_log("browser"):
     log = f'{entry["level"]}: {entry["source"]}: {entry["message"]} [{str(datetime.fromtimestamp(int(entry["timestamp"])//100))}]'
     print(log)
     dat += log+"\n"

print("done!")
print("writing to file...")

with open("debug.log", "w") as logfile:
    logfile.write(dat)

driver.close()


