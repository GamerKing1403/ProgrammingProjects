from selenium import webdriver
from selenium.common import exceptions

driver = webdriver.Chrome('C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.get("https://www.instagram.com")
while True:
    try:
        button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        button.send_keys('tusharjain1903@gmail.com')
        button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        button.send_keys('TushTanSurDhi14032003')
        button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        button.click()
        break
    except:
        continue

while True:
    try:
        button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        button.click()
        break
    except:
        continue