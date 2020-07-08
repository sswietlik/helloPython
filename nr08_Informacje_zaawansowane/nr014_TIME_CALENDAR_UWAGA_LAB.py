import time
print(time.time())

print(time.localtime())
print(time.localtime(time.time()))

import calendar
print(calendar.month(1984,4))

calendar.setfirstweekday(6)
print(calendar.month(1984,4))

print(calendar.isleap(2000))
calendar.setfirstweekday(0)
print(calendar.calendar(2019))
