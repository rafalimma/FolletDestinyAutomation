from xml.dom.minidom import Element
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from pathlib import Path

WAIT_TIME = 4
ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
) # navegador
chrome_browser.get('https://iscbrazil.follettdestiny.com/portal/portal?app=Library%20Manager')

barcode = "2003"

time.sleep(5)
print('aqui ta indo')
circulation_button = WebDriverWait(chrome_browser, WAIT_TIME).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Circulation')]"))
)
circulation_button.click()

chrome_browser.switch_to.frame("Library Manager")

sidebar_checkin = WebDriverWait(chrome_browser, WAIT_TIME).until(
    EC.visibility_of_element_located((By.ID, "Check In"))
)
sidebar_checkin.click()
time.sleep(3)

barcode_input = WebDriverWait(chrome_browser, WAIT_TIME).until(
    EC.element_to_be_clickable((By.NAME, 'barcode'))
)
barcode_input.click()
barcode_input.send_keys(barcode + Keys.RETURN)

print('Check in feito')

chrome_browser.switch_to.default_content()

home_button = WebDriverWait(chrome_browser, WAIT_TIME).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Home')]"))
)
home_button.click()