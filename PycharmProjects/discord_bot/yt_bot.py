import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.youtube.com/watch?v=exy1Ok3ZIVc')

while True:
    try:
        driver.find_element_by_id('player-container').click()
        break
    except NoSuchElementException:
        continue

while True:
    time.sleep(5)
    driver.refresh()
