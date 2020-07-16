import random

myNumbers = []

while len(myNumbers) < 7:

    newNumber = random.randint(1,49)
    # bez dublowania
    if newNumber in myNumbers:
        print('doubled number is :',newNumber, ', next draw')
        continue
    myNumbers.append(newNumber)
    print(myNumbers)