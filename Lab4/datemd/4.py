from datetime import datetime

date1 = datetime(2025, 2, 13, 11, 8, 2)  
date2 = datetime(2025, 2, 11, 7, 15, 6)  

print(date1)
print(date2)
difference = date1 - date2

secondsdifference = difference.total_seconds()

print("Difference in seconds:", int(secondsdifference))
