from selenium import webdriver  # importing all the important drivers
from webdriver_manager.chrome import ChromeDriverManager
import time

# defining a variable to hold the Starting website
start_url = "https://music.youtube.com/playlist?list=LM"

# Creating all the options required to start the chrome with a custom user
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(r'--user-data-dir=C:\Users\user\Documents\ProgrammingProjects\SeleniumChromeProfile')

# Creating the main driver and getting the webpage
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get(start_url)

# just to wait for the website to open
time.sleep(5)

# a loop for
for i in range(1, 632):
    button = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-browse-response/'
                                          'ytmusic-section-list-renderer/div[2]/ytmusic-playlist-shelf-renderer/div[1]'
                                          '/ytmusic-responsive-list-item-renderer[{}]/ytmusic-menu-renderer/paper-icon'
                                          '-button'.format(i))
    button.click()
    button = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown[1]/div'
                                          '/ytmusic-menu-popup-renderer/paper-listbox/'
                                          'ytmusic-menu-navigation-item-renderer[2]/a')
    button.click()
    time.sleep(1)
    button = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown[2]/div/'
                                          'ytmusic-add-to-playlist-renderer/div[1]/'
                                          'ytmusic-playlist-add-to-option-renderer[1]')
    button.click()
