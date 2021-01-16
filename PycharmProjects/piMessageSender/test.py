from datetime import datetime as dt
import datetime

today = dt.today()
currentDay = dt.date(today).isocalendar()
nxt_sunday_date = today.day + (7 - currentDay[2])
nxt_sunday = dt(year=today.year, month=today.month, day=16, hour=23, minute=50, second=0)
print(today)
print(nxt_sunday)
difference = (nxt_sunday - today)
total_seconds = difference.total_seconds()
print(total_seconds)