from datetime import date

def DaysToEnd(year=date.today().year, month=date.today().month, day=date.today().day):

    date_today = date(year,month,day)
    date_end_of_year = date(year,12,31)
    delta = date_end_of_year - date_today
    print('Counting from ', date_today,'days remaining', delta.days)


DaysToEnd()
DaysToEnd(year=2020)
DaysToEnd(2020,12,20)
DaysToEnd(day=20,month=12,year=2020)
DaysToEnd(day=1)
