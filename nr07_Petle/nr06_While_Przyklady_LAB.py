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
print('Wystąpil problem z kodem do zweryfikowania ')
#
# import random
# my_number = random.randint(0,20)
# guess = -1
# trials = 0
#
# print('Guess my number!')
#
# while guess != my_number:
#     guess=int(input())
#     trials+=1
#     if guess == my_number:
#         print('Gratulacje', my_number)
#     elif guess > my_number:
#         print('Sorry my number is smaller than your guess, Try again!',guess)
#     else:
#         print('Sorry- my number is greater than your guess, Try again!',guess)
# -------------------------------------------------------------------
print('Zad 3')
print()

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
i = 0

max = len(texts)-1


while i < max:
    print(i, texts[i],texts[i+1])

if len(texts[i]) == len(texts[i+1]):
    print("\tFOUND")

i+=1

