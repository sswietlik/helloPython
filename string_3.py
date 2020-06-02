somethingLikeNumber='1000'
print(somethingLikeNumber +" " "to nie jest liczba a python wie że to jest tekst")

print()
print(int(somethingLikeNumber)+1)
print("powyższy zapis potraktował zmienną somethingLikeNumber jako 'int' czyli \n \t liczbę i dodał inną liczbę")
print()

print("badam typ/klasę zmiennej używając funkcji type()")
print(type(somethingLikeNumber)) #użycie funkcji type() pozwala na zbadanie z jakim rodzajem zmiennej mamy do czynienia
print()

print("badam typ zmiennej po konwersji na inny rodzaj w tym przypadku liczbowy")
print(type(int(somethingLikeNumber)))
