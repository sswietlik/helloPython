def DaysToEnd():
    from datetime import date

    currentYear = date.today().year
    days_In_aYear = date(currentYear,12,31)
    print(days_In_aYear - date.today())
DaysToEnd()
