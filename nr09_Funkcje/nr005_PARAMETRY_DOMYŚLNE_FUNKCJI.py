from datetime import date
from datetime import timedelta

# def GivenWorkingDay(year=date.today().year,month=date.today().month,day=date.today().day):
def GivenWorkingDay(year,month=1,day=1):    #nadaję wartość domyślną dla przypadku kiedy będzie brakowało tego parametru



    day = date(year,month,day)
    # day = date(2020,7,18)
    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day
    print('nearest working day is: ',workingday)
    return

GivenWorkingDay(2020,8)
GivenWorkingDay(2020,8,1)  #w tym przypadku wartość domyślna funkcji jest zastąpiona poprzez wartość podaną czyli w tym przypadku DZIEŃ
GivenWorkingDay(2020)     #wywołana funkcja korzysta z wartości domyślnej