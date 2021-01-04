from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import schedule
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

# name = input('Enter the name of user or group : ')
# msg = input('Enter your message : ')
#
# input('Enter anything after scanning QR code')


def job(t):
    user = driver.find_element_by_xpath('//span[@title = "Rounauk Frnd"]')
    user.click()

    msg_box = driver.find_element_by_class_name('_13mgZ')
    msg_box.send_keys("*Happy Birthday And Many Many Happy Returns Of the Day*\n This is An Automated text Message And "
                      "If You Want The Code msg Me I Will Send It In The Morning....With Some Comments")
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    return


schedule.every().day.at("23:59:59").do(job, "It is Working")

while True:
    schedule.run_pending()
    time.sleep(2)  # wait one minute
