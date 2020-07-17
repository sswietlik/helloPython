colours = ['Hearts','Diamonds','Clubs','Spades']
figures =[
    {'Figure':'Ace',      'Power': 14},
    {'Figure':'King',     'Power': 13},
    {'Figure':'Queen',    'Power': 12},
    {'Figure':'Jack',     'Power': 11},
    {'Figure':'10',       'Power': 10},
    {'Figure':'9',        'Power': 9}]

allCards = []
for c in colours:
    for f in figures:
        aCard = f.copy()
        aCard['Color']=c
        allCards.append(aCard)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]


print('---------1---------')
print(player1)
print('---------2---------')
print(player2)

while len(player1) > 0 and len(player2) >0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    stack= []

#             WOJNA
    if card1['Power'] == card2['Power']:
        while card1['Power'] == card2['Power']:

            print('WAR',card1,['Power'],card2['Power'])
            stack.append[card1]
            stack.append[card2]

            if len(player1)<2:
                player2.extend(stack)
                player2.extend(player1)
                player1=[] #sprawdz p1=[]
                print('p1',player1,'p2',player2)#moja wersja
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')

                break
            elif len(player2)<2:
                player1.extend(stack)
                player1.extend(player2)
                player2=[] #sprawdz p1=[]
                print('p2',player2,'p1',player1)#moja wersja
                print('PLAY-1 \t %d \t %d \t' % (card2["Power"], card1["Power"]) + len(player1)*'*')
                break
            else:
                card1 = player1.pop(0) # (to te karty, które kładzie się na stosie, ale króre niczego nie zmieniają)
                card2 = player2.pop(0)
                stack.append(card1)
                stack.append(card2)

                card1 = player1.pop(0) #te karty są już właściwe
                card2 = player2.pop(0)

        else:
            if card1['Power'] > card2['Power']: #sprawdzam czy c1p1>c2p2 ?
                stack.append(card1)             #jeśli tak to : do stak wrzucam karty obu graczy
                stack.append(card2)
                player1.extend(stack)           # zwiększam karty  gracza 1 z bufora stack
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')

            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2) * '*')
    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)

        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card1)
        player2.append(card2)

        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2) * '*')

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')
# print('WOJNA')
            # player1.append(card1+1)
            # print(player1.append(card1+1)




#         player1.append(card1)
#         player2.append(card2)
#         print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
#
#     elif card1['Power'] > card2['Power']:
#         player1.append(card1)
#         player1.append(card2)
#         print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
#     else:
#        player2.append(card2)
#        player2.append(card1)
#        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
# if len(player1) >  0:
#     print('P1 Wonn')
# else:
#     print('P2 Wonn')

# ~~~~~~~~~~~~~~WOJNA~~~~~~~~~~~~~~


