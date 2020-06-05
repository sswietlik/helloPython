helloMessage1 = "Hello %s!"
print(helloMessage1 %'Kate')
print(helloMessage1 %'Chris')

print()
helloMessage2= "Hello {0:s}"
print(helloMessage2.format('Chris'))
print(helloMessage2.format('Kate'))
print()
helloMessage3 = "%5s has %7d %7s"
print('komunikat 1')
print(helloMessage3 % ('Kate',1,'animal'))
print(helloMessage3 % ('Chris',1000,'$'))
print()
print("Komunikat 1 - użycie FORMAT")
helloMessage3 = "{0:s} has {1:d} {2:s}"
print(helloMessage3.format('Kate',1,'animal'))
print(helloMessage3.format('Chris',1000,'$'))
print()
line="%20s cost %6d EUR"
print(line %('ICE CREAM',3))
print(line %('TRIP TO VENICE',119))
print(line %('PIZZA HAWAI',6))
print()
print('wersja 2')
line2='{0:20s} cos {1:6d} EUR'
print(line2.format('ICE CREAM',3))
print(line2.format('TRIP TO VENICE',119))
print(line2.format('PIZZA HAWAI',6))