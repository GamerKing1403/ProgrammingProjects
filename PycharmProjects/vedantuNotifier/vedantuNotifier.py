from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import exceptions
from os.path import abspath
from os import path
import getpass

start_url = "https://www.vedantu.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(r'--user-data-dir=C:\Users\user\Documents\ProgrammingProjects\SeleniumChromeProfile')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get(start_url)
winHandelBefore = driver.window_handles[0]
button = driver.find_element_by_id('login-link')# Finds the Login link button
button.click()
while True:# used to over come for it to try to click when the page is loading
    try:
        button = driver.find_element_by_xpath('//*[@id="signInWithGoogle"]')  # Finds the google sign in button
        button.click()
        break
    except exceptions.NoSuchElementException :
        continue

while True:# used to over come for it to try to click when the page is loading
    try:
        button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/nav/div[2]/div[1]/div/div[3]/div/a')# Finds the calender tab
        button.click()
        break
    except exceptions.NoSuchElementException :
        continue

while True:# used to over come for it to try to click when the page is loading
    try:
        button = driver.find_element_by_class_name('fc-today')
        print(button.get_attribute("value"))
        break
    except exceptions.NoSuchElementException :
        continue
# rowCount = len(driver.find_element_by_xpath('//*[@id="my-calendar-section"]/div[3]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr'))
# colCount = len(driver.find_element_by_xpath('//*[@id="my-calendar-section"]/div[3]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[1]/td'))
# print(rowCount)
# print(colCount)

rows_count = driver.execute_script("return document.getElementsByTagName('tr').length")
columns_count = driver.execute_script("return document.getElementsByTagName('tr')[0].getElementsByTagName('th').length")
print(rows_count)
print(columns_count)

#
# first_part = "//*[@id='post-body-6522850981930750493']/div[1]/table/tbody/tr["
# second_part = "]/td["
# third_part = "]"

# for i in range

#
# //*[@id="my-calendar-section"]/div[3]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]
# //*[@id="my-calendar-section"]/div[3]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[1]
# //*[@id="my-calendar-section"]/div[3]/div[2]/div/table/tbody/tr/td/div/div/div[3]
# driver.close()
