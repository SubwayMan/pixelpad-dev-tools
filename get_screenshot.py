import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

site = sys.argv[1]

opt = webdriver.ChromeOptions()
opt.add_argument("headless")
opt.add_argument('--ignore-certificate-errors')
opt.add_argument("--test-type")

PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH, chrome_options=opt)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

driver.get(site)

dest = os.path.join(os.getcwd(), "screenshots")
driver.save_screenshot("test.png")
'''
id = 1
while True:
    fname = os.path.join(dest, "screenshot"+str(id)+".png")
    if not os.path.exists(fname):
        driver.save_screenshot(fname)
        break
    id += 1
'''

driver.close()


