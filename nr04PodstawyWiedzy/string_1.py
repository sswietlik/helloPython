atext='This is a text.'
atexSum='Thisisatext'
print(atext.endswith('ext'))
print(atext.endswith('ext.'))

print(atext.islower())

print(atext.upper())

print(atext.upper().isupper())

print(atext.find('is'))

print(atext.find('is',3)) #3 od którego znaku program ma szukać początku "is"

print(atexSum.replace('a','@').replace('s','5').replace('i','1').replace('e','3'))

print(atext.split(' '))

somethingLikeNumber='1000'
# somethingLikeNumber+1

#funkcje badajace czy coś jest liczbą
print(somethingLikeNumber.isdigit()) #czy ten napis wygląda jak liczba i można ją przekonwertować
print(somethingLikeNumber.isdecimal()) #czy jest to liczba z przecinkiem
print(somethingLikeNumber.isalpha()) #czy napis składa się z samych liter
print(somethingLikeNumber.isalnum()) #czy napis sklada sie z liter i/lub cyfr




