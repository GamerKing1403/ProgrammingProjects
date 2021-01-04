from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code')
#
# user = driver.find_element_by_xpath('//span[@title="Katie Discord"]')
# user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(5):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    print(count)