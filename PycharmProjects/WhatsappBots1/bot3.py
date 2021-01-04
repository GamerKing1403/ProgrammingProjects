from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import exceptions

# Creates the web driver.
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
driver.maximize_window()

# The Main Function
if __name__ == '__main__':
    # Takes all the inputs
    name = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))
    while True:
        try:
            driver.find_element_by_xpath('//span[@title = "'+name+'"]').click()
            break
        except exceptions.NoSuchElementException:
            continue

    msg_box = driver.find_element_by_class_name('_13mgZ')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
        print(count)
driver.close()
