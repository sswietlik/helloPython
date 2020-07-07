import random

for i in range(1,10):
    print(random.randint(1,100))
print('-------------------------------')
print()

number1=random.randrange(1,100)
print('The first generated number is %d' %(number1))

counter = 1
number2=random.randrange(1,100)
#
# print(counter)
# print(number2)

while number1 != number2:
    counter += 1
    number2 = random.randrange(1, 100)
    print(counter,number2)
print("I needed %d attempts to generate %d again" % (counter, number1))
print('-------------------------------')
print()

print('FIFA WORLD CUP RUSSIA 2018')

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries) #losowo wymieszaj kolejność drużyn
groupNumber = 0  #utwórz zmienną groupNumber i przypisz jej wartość 0
for i in range(len(countries)): #wykonaj czynność tyle razy ile jest państw na liście countries:
    if i % 4 == 0:
        groupNumber += 1
        print('----GRUPA %d----'%(groupNumber))
    print(countries[i])
