import random

myNumbers = []

while len(myNumbers) < 7:

    newNumber = random.randint(1,49)

    myNumbers.append(newNumber)
    print(myNumbers)