from datetime import date
from datetime import timedelta



day = date.today()
# day = date(2020,7,18)
if day.weekday() == 5:
    workingday = day + timedelta(days=2)
elif day.weekday() == 6:
    workingday = day + timedelta(days=1)
else:
    workingday = day
print(workingday)