from datetime import date

def DaysToEnd(*dates):

    for date_today in dates:
        print()


    date_end_of_year = date(date_today.year,12,31)
    delta = date_end_of_year - date_today
    print('Date', date_today, 'days to end of year', delta.days)


DaysToEnd(date(1999,1,15))
print('----------------')
DaysToEnd(date(1999,1,15),date(2009,1,15))
print('----------------')
DaysToEnd(date(1999,1,15),date(2009,1,15),date(2019,1,15),date.today())



