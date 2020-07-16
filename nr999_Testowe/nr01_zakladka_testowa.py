colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace', 'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10', 'Power': 10},
    {'Figure': '9', 'Power': 9},
    {'Figure': '8', 'Power': 8},
    {'Figure': '7', 'Power': 7},
    {'Figure': '6', 'Power': 6},
    {'Figure': '5', 'Power': 5},
    {'Figure': '4', 'Power': 4},
    {'Figure': '3', 'Power': 3},
    {'Figure': '2', 'Power': 2},
    {'Figure': '1', 'Power': 1}]

allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 1--------')
print(player2)

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        # print('=EQUAL \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        # print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    else:
        player2.append(card2)
        player2.append(card1)
        # print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')