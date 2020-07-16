# serce - kier / hearts
# dzwonki - karo / diamonds
# żołądź - trefl / clubs
# wino - pik / spades

import random

colours = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

allCards =[]

for c in colours:
    for f in figures:
        allCards.append('%s - %s' %(c,f))
print(allCards)

random.shuffle(allCards)
print(allCards)


player1=[]
player2=[]

max = len(allCards)

for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print('--PLAYER nO-1')
print(player1)

print('--PLAYER nO-2')
print(player2)


