import time

# sprawdzenie wersji pythona
import sys

print(sys.version)

# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
# print(time.perf_counter(), time.localtime(time.perf_counter()))

print(time.time())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

print(time.localtime(time.perf_counter()))

import calendar

print('-------------------------------------')
print(calendar.month(2020,7,5,2))
# wyświetlam kalendarz  (rok,miesiac, 5znaków na każdy dzień , odstępy miedzy liniamia 2

print('-------------------------------------')
print(calendar.month(2020,7))

print('-------------------------------------')
print(calendar.weekday(2017,9,29))

print('-------------------------------------')
calendar.setfirstweekday(6) #podaję niedzielę jako pierwszy dzień wyświetlanego kalendarza
print(calendar.month(2020,7))
calendar.setfirstweekday(0)
print(calendar.month(2020,7))

print('-------------------------------------')
print(calendar.isleap(2020)) #czy dany rok jest przestępny ?

print('-------------------------------------')
print('ile bylo dni przestepnych w tych latach ',calendar.leapdays(2000,2017))
print('ile bylo dni przestepnych w tych latach ',calendar.leapdays(2000,2020))
print('ile bylo dni przestepnych w tych latach ',calendar.leapdays(2000,2021))

print('-------------------------------------')
print(calendar.calendar(2020))

