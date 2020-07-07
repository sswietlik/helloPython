import math

print('reczne kalkulacje')
degree = 360
radian = degree * math.pi/180
print(radian)
print('wynik ponizej jest to wykorzystanie moułu radians')
print(math.radians(degree))
print()

print('reczne kalkulacje')
degree=45
radian = degree * math.pi/180
print(radian)
print('wynik ponizej jest to wykorzystanie moułu radians')
print(math.radians(degree))
print()

print('PIZZA')
sPizza_r=0.22
mPizza_r=0.27
bPizza_r=0.38

sPizzaPrice=11.50
mPizzaPrice=15.60
bPizzaPrice=22.00


print()
print('PIZZA AREA [m2]')
sPizzaArea=round(math.pi*sPizza_r**2,2)
mPizzaArea=round(math.pi*mPizza_r**2,2)
bPizzaArea=round(math.pi*bPizza_r**2,2)

print(sPizzaArea)
print(mPizzaArea)
print(bPizzaArea)
print()

sPizzaPerM2 = sPizzaPrice/sPizzaArea
mPizzaPerM2 = mPizzaPrice/mPizzaArea
bPizzaPerM2 = bPizzaPrice/bPizzaArea

print(sPizzaPerM2)
print(mPizzaPerM2)
print(bPizzaPerM2)