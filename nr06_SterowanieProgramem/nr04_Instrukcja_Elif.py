likes = 50
shares = 1000

if likes <  500:
    print('no enough likes')
else:
    if shares <100:
        print('Likes OK, but you need more shares')
    else:
        print('DISCOUNT accepted')
print('END')
print()

likes = 500
shares = 10

if likes < 500:
    print('no enough likes')
elif shares  < 100:
    print('no enough shares')
else:
    print('you have discount')
print()

print('Zadanie2-A')
pizza = True
bigDrink = False
isWeekend = False

if not isWeekend and (pizza or bigDrink):
    print('free burger')
else:
    if isWeekend:
        print('is weekend come back between mo-fri')
    else:
        if not pizza or bigDrink: print('need order pizza or bigDrink')
print()

print('Zadanie2-B')
pizza = False
bigDrink = False
isWeekend = False

if not isWeekend and (pizza or bigDrink):
    print('free burger')
elif isWeekend:
    print('is weekend come back MO-FR')
else:
    print('need order pizza or bigDrink')