print('Zad 1')
print()

number = 1
previousNumber = 0
while number <= 50:
    print(number,'+', previousNumber,'=',number + previousNumber)
    previousNumber=number
    number+=1
print()

# -------------------------------------------------------------------
print('Zad 2')
print()

import random
my_number = random.randint(0,20)
guess = -1
trials = 0

print('Guess my number!')

while guess != my_number:
    guess=int(input())
    trials+=1
    if guess == my_number:
        print('Gratulacje', my_number)
    elif guess > my_number:
        print('Sorry my number is smaller than your guess, Try again!',guess)
    else:
        print('Sorry- my number is greater than your guess, Try again!',guess)



