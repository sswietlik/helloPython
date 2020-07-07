line='this IS a very STRANGE text'
print(line.capitalize()) #teskt skonwertowany do zdania zaczynajacego sie od duzej litery

print(line.title()) # Każde słowo zaczyna się od DUŻEJ litery

print(line.upper()) #Wszystkie słowa są z DUŻEJ litery

print(line.lower())#Wszystkie słowa są z MAŁEJ litery

print(line.swapcase()) #Zamienia WIELKOŚCI LITER

print(line.casefold())
line='der Fluß'
print(line,'     casefold zamienia literę ß na SS')
print(line.casefold())

line = 'ŻÓŁĆ'
print(line.lower())#Wszystkie słowa są z MAŁEJ litery
print(line.casefold())

print(line.replace('Ż','Z').replace('Ó','O').replace('Ł','L').replace('Ć','C').lower())




