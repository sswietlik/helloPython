countries = ['FR','US','DE','RU']
print(countries)
print(countries[0])
print(countries[1])
print(countries[2])
print(countries[3])


countries.append(('PL')) # dodawanie do listy do nastepnej pozycji
print(countries[4])

countries.insert(2,'ES') # Wstawianie w konkretną pozycję
print(countries)

countries.remove(('RU')) # Usuwa pozycję z listy
print(countries)

countries.sort() # Sortuje
print(countries)

countries.reverse() # Odwrotne sortowanie
print(countries)

print(countries.pop(2)) # POP pokazuje daną pozycję a następnie ją usuwa z listy
print(countries)

print(countries.index('PL')) #sprawdzam czy element występuje i pokazuje jego pozycję

print(countries.count('DE')) # sprawdza ile razy element wystepuje na danej liście

newList = ['FI','SE'] #Tworzy nową listę
countries.extend(newList) # Dodaje nową listę do już istniejącej
print()
countriesCopy = countries
# countriesCopy.clear()  # To polecenie czyści listę kopiowaną ale jednoczeńnie kasuje zawartość głównej listy
print()
countriesCopy = countries.copy() #Jest to nowa kopia którą można kasować lub modyfikować
countriesCopy.clear()

print(countries)
print(countriesCopy)