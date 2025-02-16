from datetime import datetime

currentdate = datetime.now()

datetimewithoutmicroseconds = currentdate.replace(microsecond=0)

print("Original Datetime:", currentdate)
print("Datetime without Microseconds:", datetimewithoutmicroseconds)
