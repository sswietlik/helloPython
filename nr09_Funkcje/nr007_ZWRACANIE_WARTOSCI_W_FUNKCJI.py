from datetime import date
from datetime import timedelta

def GivenWorkingDay(year=date.today().year,month=date.today().month,day=date.today().day):


    day = date(year,month,day)
    # day = date(2020,7,18)
    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    return workingday

nextWorkinDay = GivenWorkingDay(2020,7,25)
print('next working day after', GivenWorkingDay(), 'is : ', nextWorkinDay)
nextWorkinDay = GivenWorkingDay()
print('next working day after is : ', GivenWorkingDay())