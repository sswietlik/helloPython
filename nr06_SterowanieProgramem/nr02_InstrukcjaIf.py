print("@#-10% DISCOUNT")
like = 500
share = 100
discount = 0.1


if like>=500 and share >=100:
    print("Discount is -10%")
else:
    print("No discount")
print()

print("@# FREE BURGER PROMOTION")
workingDays = False
Pizza = True
BigDrink = True

if workingDays and Pizza or BigDrink:
    print("Free Burger")
else:
    print("No promotion")
print()


print("FREE HDD SPACE")
diskSize = 140
diskSizeUsed = 133
fileSize = 10

if diskSize-diskSizeUsed>=fileSize:
    print("File can be downloaded")
else:
    print("Not enough free space on hardDrive")
