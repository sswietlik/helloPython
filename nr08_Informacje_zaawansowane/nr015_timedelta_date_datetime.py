import datetime

print('Minimum and maximum',datetime.MINYEAR, datetime.MAXYEAR)


# Ktoś mówi że zrobi coś za 1 dzień 1h i  30 minut

d1 = datetime.timedelta(days=1,hours=1,minutes=-30)
print(d1)

d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3)
print(d2)

print(d1+d2)

# DATA
print('Today is', datetime.date.today())
today=datetime.date.today()
daysToPay= datetime.timedelta(days=7)
print(today)
print(today+daysToPay)

endOfTheWorld = datetime.date.max
print(endOfTheWorld)
# oneDayLater = datetime.timedelta(days=1)
# print(endOfTheWorld+oneDayLater)
print(endOfTheWorld.weekday())

bornDate = datetime.date(2000,8,15)
todayIs = datetime.date(2017,9,29)
print(todayIs-bornDate)

# from datetime import datetime

print('now()\t\t',datetime.datetime.now())
print('today()\t\t',datetime.datetime.today())
print('utcnow()\t',datetime.datetime.utcnow())
print('weekday()\t',datetime.datetime.today().weekday())

# konwersja np dni tygodnia %a oznacza dzień tygodnia w skrócie a %A opis pełnej nazwy dnia

print('%a\t\t\t',datetime.datetime.now().strftime('%a'))
print('%A\t\t\t',datetime.datetime.now().strftime('%A'))
print('%w\t\t\t',datetime.datetime.now().strftime('%w'))

print('%a %A %w \t',datetime.datetime.now().strftime('%a, %A, %w'))


