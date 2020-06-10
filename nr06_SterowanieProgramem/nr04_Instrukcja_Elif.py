likes = 500
shares =100

if likes >=500 and shares >=100 :
    print("Disc -10% accepted")
else:
    print('disc not accepted')
print()


print('z wykorzystaniem elif')
likes = 600
shares =50
if likes >=500 and shares >=100:
    print('you have -10%')
elif  likes<=500:
    print('need more likes')
elif  shares <=100:
    print('need more shares')
print()

print("xxx")
isWeekend = False
bigDrink =False
pizza = True

if (pizza or bigDrink) and not isWeekend:
    print("free burger")
else:
    if isWeekend:
        print('przyjdź po weekendzie')
    else:
        print("kup pizze lub napój")
print()

print("promocja na darmowego burgera 2 z zastoswaniem elif")
isWeekend = True
bigDrink =False
pizza = False
if not isWeekend and (pizza or bigDrink):
    print("free burger")
else:
    if isWeekend:
        print("wróć po weekendzie")
    else:
        print("kup pizze lub duży napój ")




