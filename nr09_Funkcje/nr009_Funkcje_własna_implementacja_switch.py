def WeekDayInFrench(dayNumber):

    names = {
        0: 'lundi',
        1: 'mardi',
        2: 'mercredi',
        3: 'jeudi',
        4: 'vendredi',
        5: 'samedi',
        6: 'dimanche',
    }

    return names.get(dayNumber, 'ERROR')
    #  żeby otrzymać odpowiednią wartość
    # dla zmiennej NAMES wywołuję metodę GET
    # metoda GET z listy NAMES ma wybrać DAYNUMBER a jeśli nie znajdzie to ERROR

print(WeekDayInFrench(0))
print(WeekDayInFrench(1))
print(WeekDayInFrench(2))
print(WeekDayInFrench(3))
print(WeekDayInFrench(4))
print(WeekDayInFrench(5))
print(WeekDayInFrench(6))
print(WeekDayInFrench(7))