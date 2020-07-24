def DaysToEndOfYear(year,month,day):
    from datetime import date

    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)


DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year=2022,month=12,day=22)
DaysToEndOfYear(day=23,month=12,year=2023)