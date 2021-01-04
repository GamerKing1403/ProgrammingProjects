from selenium import webdriver
from selenium.common import exceptions

driver = webdriver.Chrome('C:\\Users\\user\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')

driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
while True:
    try:
        button = driver.find_element_by_class_name('_2zCfw')
        break
    except exceptions.NoSuchElementException:
        continue

button.click()
button.send_keys(name)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
button = driver.find_element_by_class_name('_3H4MS')
button.click()
msg_box = driver.find_element_by_class_name('_13mgZ')
msg_box.send_keys(msg)
button = driver.find_element_by_class_name('_3M-N-')
button.click()

# driver.close()
