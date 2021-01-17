import json
import requests
from datetime import datetime as dt
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


slack_token = 'xoxb-1546263022019-1569905814384-VwVfQLvSwSUpZ9OWtdV6GyHb'
slack_channel = '#notifications-from-computers'
slack_user_name = 'Notifications'


today = dt.today()
currentDay = dt.date(today).isocalendar()
nxt_sunday_date = today.day + (7 - currentDay[2])
nxt_sunday = dt(year=today.year, month=today.month, day=nxt_sunday_date, hour=22, minute=25, second=0)


chromeOptions = webdriver.FirefoxOptions()
chromeOptions.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
driver.get('https://claystage.com/one-piece-chapter-release-schedule-for-{}'.format(currentDay[0]))
value = driver.find_element_by_xpath(
    "/html/body/div[1]/div/main/div/div/div/article/div/div[3]/table/tbody/tr[{}]/td[2]".format(currentDay[1])).text


def sendMessageOnTime():
    global today
    today = dt.today()
    difference = (nxt_sunday - today)
    total_seconds = difference.total_seconds()
    currentHour = today.hour
    currentMin = today.minute
    if currentHour == 22 and 25 <= currentMin <= 30 and currentDay[2] == 7:
        Message = 'New One Piece Chapter in {} mins'.format(30 - currentMin)
        post_message_to_slack(Message)
    else:
        print('going to sleep for ', total_seconds)
        time.sleep(total_seconds)
        sendMessageOnTime()


def post_message_to_slack(text, blocks=None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': text,
        'username': slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()


if __name__ == '__main__':
    try:
        int(value)
        sendMessageOnTime()
    except ValueError as e:
        pass
