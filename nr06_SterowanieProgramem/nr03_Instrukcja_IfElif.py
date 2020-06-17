age = 27
isDrunk =True
isRestrictedArea = False

textMsg1= 'Gorszy sposob'
textMsg2='Lepszy sposob'

warMsg1 = 'You are too young to buy alcohol'
warMsg2 = 'Are you drunk?, We cannot sell you alcohol'
warMsg3 = 'Restricted area. Alcohol is forbidden'
okMsg1 = 'Ok, you can buy alcohol'

print(textMsg1)
if age <18:
    print(warMsg1)
else:
    if isDrunk:
        print(warMsg2)
    else:
        if isRestrictedArea:
            print(warMsg3)
        else:
            print(okMsg1)
print()
print(textMsg2)


if age <18:
    print(warMsg1)
elif isDrunk:
    print(warMsg2)
elif isRestrictedArea:
    print(warMsg3)
else:
    print(okMsg1)