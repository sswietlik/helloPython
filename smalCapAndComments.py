# Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
# Zakladamy ze:
# -liczba mrugniec na minute to 20
# -liczba minut w godzinie to 60
# -liczba godzin w dobie 24
# -liczba lat (czyli nasz X) 50
# Uwaga: jezeli przyjac ze spimy 8 godzin to liczba godzin na dobe
# powinna wynosic 16

blinksPerMin = 20
minPerHour = 60
hoursPerDay = 24
daysInYear = 365
years = 50

print("l.mrugnięć na minutę = ", blinksPerMin)
print("l.minut w godzinie = ", minPerHour)
print("l.godzin w dobie  = ", hoursPerDay)
print("l.dni w roku = ", daysInYear)
print("l.lat = ", "X")


print(blinksPerMin*minPerHour*hoursPerDay*daysInYear*years)

print("")
print("następne zagadnienie")
print("Znajdź błąd w poniższym skrypcie (możesz skopiować skrypt i próbować go uruchomić). Błędy są 2 :)")
10.

print("   definitionOfVariables")
print("   daysOfWorkPerMonth = 20")
print("   monthsInYear = 12")
print("   vacation = 26")
print("   yearsOfWOrk = 40")
print("   result")
print("   print((daysOfWorkPermonth * monthsInYear - Vacation)*yearsOfWOrk)")
print(" ")


print("Rozwiazanie")
print(" ")
# definitionOfVariables
daysOfWorkPerMonth = 20
print("daysOfWorkPerMonth =",daysOfWorkPerMonth)
monthsInYear = 12
print("monthsInYear =",monthsInYear)
vacation = 26
print("vacation =",vacation)
yearsOfWOrk = 40
print("years of work =", yearsOfWOrk)
print(" ")

print("(daysOfWorkPerMonth * monthsInYear - vacation) * yearsOfWOrk")
print((daysOfWorkPerMonth * monthsInYear - vacation) * yearsOfWOrk)