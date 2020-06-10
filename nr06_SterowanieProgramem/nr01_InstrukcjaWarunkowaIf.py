age = 18

if age >= 18:
    print('Jesteś DOROSŁY możesz kupić alkohol')
else:
    print("NIE jesteś DOROSŁY i nie możesz kupuić alkoholu ")

isDrunk = False

if age >=18 and not isDrunk:
    print('Jesteś TRZEŹWY możesz kupić alkohol')
else:
    print("NIE jesteś TRZEŹWY i nie możesz kupić alkoholu")

isRestrictedArea = False
if age >=18 and not isDrunk and not isRestrictedArea:
    print("W tym miejscu MOŻESZ SPOŻYWAĆ alkohol")
else:
    print("W tym miejscu NIE MOŻESZ SPOŻYWAĆ alkoholu")