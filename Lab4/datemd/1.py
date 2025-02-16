from datetime import datetime, timedelta

current_date = datetime.now()

datefivedaysago = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date 5 Days Ago:", datefivedaysago.strftime("%Y-%m-%d"))
