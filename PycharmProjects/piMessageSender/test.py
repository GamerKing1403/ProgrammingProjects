# import requests
# from bs4 import BeautifulSoup
from datetime import datetime as dt
# headers = {'User-Agent': 'FooBar-Spider 1.0'}
# url = 'https://claystage.com/one-piece-chapter-release-schedule-for-{}'.format(2021)
# r = requests.get(url, headers=headers)
# r.raise_for_status()
# soup = BeautifulSoup(r.text, 'html.parser')
# soup.find_all('td', class_='col-2')[1].text


today = dt.today()
currentDay = dt.date(today).isocalendar()
print(currentDay)