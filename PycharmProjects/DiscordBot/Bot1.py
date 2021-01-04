from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import time

start_url = "https://discord.com/channels/752398003033210920/755345949399711784"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(r'--user-data-dir=C:\Users\user\Documents\ProgrammingProjects\SeleniumChromeProfile')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get(start_url)
messagebox = None
while True:
    try:
        messagebox = driver.find_element_by_class_name('slateTextArea-1Mkdgw')
        break
    except exceptions.NoSuchElementException:
        continue
count = 0
count2 = 0
while True:
    if count2 == 50:
        messagebox.send_keys("rpg buy life potion 50" + Keys.ENTER)
        count2 = 0
    if count == 3:
        messagebox.send_keys("rpg heal"+Keys.ENTER)
        count = 0
        time.sleep(2)
    messagebox.send_keys("rpg hunt"+Keys.ENTER)
    time.sleep(60)
    count += 1
    count2 += 1
