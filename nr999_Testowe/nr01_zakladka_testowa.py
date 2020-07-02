def ktoreUrodziny(rok):
    from datetime import date
    day=date.today()
    year=day.year
    roznice=[]
    for wiek in rok:
        roznica=year-wiek
        roznice.append(roznica)
    return roznice
ktoreUrodziny([1954, 1986, 1990, 1998])