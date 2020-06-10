CountryLeaders={'PL':'Duda','US':'Trump'}

print(CountryLeaders['US'])

CountryLeaders['DE']='Merkel'
print(CountryLeaders['DE'])
print()
print('Keys')
print(CountryLeaders.keys())
print()
print('Values')
print(CountryLeaders.values())
print()
print('Items')
print(CountryLeaders.items())
print()

print(CountryLeaders.setdefault('FR','Macron')) #dodaje wartość domyślną

print(CountryLeaders.get('RU')) #brak takiego kraju dlatego wypluwa NONE
print()

NewLeaders = {'RU':'Putin','DE':'Shultz'}
print('New Leaders')
print(NewLeaders)
print()

CountryLeaders.update(NewLeaders) #aktualizuje listę o wartości z innej listy

print('CountryLeaders')
print(CountryLeaders)
