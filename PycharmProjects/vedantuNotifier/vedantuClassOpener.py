from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import exceptions
from os.path import abspath
from os import path
import getpass
import time

start_url = "https://www.vedantu.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(r'--user-data-dir=C:\Users\user\Documents\ProgrammingProjects\SeleniumChromeProfile')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get(start_url)
while True:# used to over come for it to try to click when the page is loading
    try:
        button = driver.find_element_by_id('login-link')  # Finds the Login link button
        button.click()
        break
    except exceptions.NoSuchElementException :
        continue

while True:# used to over come for it to try to click when the page is loading
    try:
        button = driver.find_element_by_xpath('//*[@id="signInWithGoogle"]')  # Finds the google sign in button
        button.click()
        break
    except exceptions.NoSuchElementException :
        continue
print("Working")
while True:
    start = time.time()
    print(start)
    try:
        button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div/div/div/div[1]/div')
        button.click()
        break
    except exceptions.NoSuchElementException:
        end = time.time()
        print(start-end)
        if end - start > 5:
            break
        break
driver.close()