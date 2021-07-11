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
driver = webdriver.Chrome(PATH, options=opt)
driver.get(site)

original_size = driver.get_window_size()
required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
required_height = driver.execute_script('return document.body.parentNode.scrollHeight')

driver.set_window_size(required_width, required_height)

dest = os.path.join(os.getcwd(), "screenshots")
if not os.path.exists(dest):
    os.mkdir(dest)

id = 1
while True:

    fname = os.path.join(dest, "screenshot"+str(id)+".png")
    if not os.path.exists(fname):
        driver.find_element_by_tag_name('body').screenshot(fname)
        break

    id += 1

driver.close()


