from selenium import webdriver
from selenium.common import exceptions

# count = int(input("The Number of Times U Want To Send The Message"))
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

# name = input("name of the server.")
test_name = "Apps, Anime & Manga United"
scroller_xpath = '//*[@id="app-mount"]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[4]/div'

driver = webdriver.Chrome('C:\\Users\\user\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
driver.maximize_window()
driver.get('https://discordapp.com/login')  # opens the page

driver.find_element_by_class_name("inputDefault-_djjkz").send_keys("tusharmicrosoft2@gmail.com")  # enters the email

button = driver.find_element_by_class_name("input-cIJ7To[type='password']")  # finds the password holder
button.click()
button.send_keys("Tushki2003")  # enters the password

driver.find_element_by_class_name("button-38aScr[type='submit']").click()  # finds the submit button

while True:
    try:
        driver.find_element_by_xpath('//a[@aria-label="'+test_name+'"]').click()
        # finds the server
        break
    except exceptions.NoSuchElementException:
        continue

scroll_view = driver.find_element_by_xpath(scroller_xpath)

driver.execute_script("document.querySelector('div[class=\"scroller-2wx7Hm\"]').scrollTop = 500")

# driver.close()
