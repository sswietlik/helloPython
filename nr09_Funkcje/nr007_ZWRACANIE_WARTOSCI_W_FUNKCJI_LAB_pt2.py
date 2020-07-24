from datetime import date

def DaysToEnd(  year=date.today().year,
                month=date.today().month,
                day=date.today().day):

    date_today = date(year,month,day)
    date_end_of_year = date(year,12,31)
    delta = date_end_of_year - date_today
    return delta.days

print(DaysToEnd(2020,12,20))
print(DaysToEnd(2020,12,21))

