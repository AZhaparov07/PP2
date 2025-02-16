from datetime import datetime, timedelta

todaydate = datetime.now()

yesterdaydate = todaydate - timedelta(days=1)
tomorrowdate = todaydate + timedelta(days=1)

print("Yesterday:", yesterdaydate.strftime("%Y-%m-%d"))
print("Today:", todaydate.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrowdate.strftime("%Y-%m-%d"))
