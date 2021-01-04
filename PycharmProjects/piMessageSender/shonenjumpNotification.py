import json
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

dict = {'username': 'GamerKing1403', 'password': 'GamerKing1403'}

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')
chromeOptions.add_argument(r'--user-data-dir=C:\Users\user\Documents\ProgrammingProjects\SeleniumChromeProfile')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)

driver.get('https://www.viz.com/account/manage_membership')

button = driver.find_element_by_id('try_login')
button.send_keys(dict['username'])
button = driver.find_element_by_id('try_pass')
button.send_keys(dict['password'])
button = driver.find_element_by_xpath('/html/body/div[7]/form/div[4]/div/input')
button.click()

print(driver.get_screenshot_as_png())

slack_token = 'xoxb-1546263022019-1569905814384-VwVfQLvSwSUpZ9OWtdV6GyHb'
slack_channel = '#notifications-from-computers'
slack_user_name = 'Notifications'

Message = ''


def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': text,
        'username': slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()


# post_message_to_slack(Message)




