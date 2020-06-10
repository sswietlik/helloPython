age = 27
isDrunk =False
isRestrictedArea = True
if age <18:
    print('za mlody')
else:
    if isDrunk:
        print('Pijany nie dostanie alko')
    else:
        if isRestrictedArea:
            print('nie chlej tu')
        else:
            print("dostanie alko może pić tu ")
print('jakas wiadomosc')
print()




print('kolejny test z użyciem elif ')
age = 27
isDrunk =False
isRestrictedArea = False


if age <18:
    print("za mlody")
elif isDrunk: # jeśli klient jest na kacu to  wyświetlamy wiadomosc a jeśli jest ok to przechodzimy do dalszej ścieżki decyzyjnej
    print('nie dostaniesz alko jestes pijany ')
elif isRestrictedArea:
    print('teren niebezpieczny grozi mandatem')
else:
    print('Wszystko ok teren bezpieczny ')