
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
# from a_selenium_get_source_from_all_frames import get_sourcecode_from_all_frames

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

# source = get_sourcecode_from_all_frames(chrome_browser )

name = 'Marques, Fagner'

time.sleep(5)
print('aqui ta indo')
circulation_button = WebDriverWait(chrome_browser, WAIT_TIME).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Circulation')]"))
)
circulation_button.click()

chrome_browser.switch_to.frame("Library Manager")

print('procurando patron name input')
patron_name_input = WebDriverWait(chrome_browser, WAIT_TIME).until(
    EC.visibility_of_element_located((By.NAME, 'searchString'))
)
patron_name_input.click()
patron_name_input.send_keys(name)

find_patron_button = WebDriverWait(chrome_browser, WAIT_TIME).until(
    EC.element_to_be_clickable((By.XPATH , "//input[@title='Find Patron']"))
)
find_patron_button.click()

print('procurando pelo link com nome  do PATRON ...')
patron_name_link = WebDriverWait(chrome_browser, WAIT_TIME).until(
    EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{name}')]"))
)
patron_name_link.click()
print('achou')

book_checkoutinput = WebDriverWait(chrome_browser, WAIT_TIME).until(
    EC.visibility_of_element_located((By.NAME, 'searchString'))
)
book_checkoutinput.click()
book_checkoutinput.send_keys("5673" + Keys.RETURN)

print('checkout feito')










