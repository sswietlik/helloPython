import math
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]



print('inputdata elements\t\t\t',inputdata.__len__())
print('factorytable elements\t\t',factortable.__len__())

if len(inputdata) == len(factortable):
    i=0
    while i<len(inputdata):
        minValue = inputdata[i]-factortable[i]*inputdata[i]
        maxValue = inputdata[i]+factortable[i]*inputdata[i]
        print('minValue = ',minValue,'\tmaxValue = ',maxValue)

        minInteger = math.floor(minValue)
        maxInteger = math.floor(maxValue)
        print('minInteger = ',minInteger,'\tn_tyelement = ',inputdata,'\tmaxInteger = ',maxInteger)
        i+=1


else:
    print("inputdata and factortable need to have equal number of elements")

print('_________________________________________________')

import random
i = 0
while i<len(inputdata):
    minValue = inputdata[i] - random.random() * inputdata[i]
    maxValue = inputdata[i] + random.random() * inputdata[i]
    print('minValue = ', minValue, '\tmaxValue = ', maxValue)

    minInteger = math.floor(minValue)
    maxInteger = math.floor(maxValue)
    print('minInteger = ', minInteger, '\tn_tyelement = ', inputdata, '\tmaxInteger = ', maxInteger)
    i += 1
print('_________________________________________________')

import datetime

todayDMY = datetime.date.today()

print(todayDMY)