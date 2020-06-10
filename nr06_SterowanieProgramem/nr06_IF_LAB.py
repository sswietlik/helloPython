musclePain= False
fever = True
weakness = True

if not musclePain and fever and weakness:
    print("suspicion of influenza")
else:
    print("The flu is unlikely")
    print()

print("Zad 2")
musclePain= False
fever = False
weakness = True
if not musclePain and fever and weakness:
    print("suspicion of influenza")
else:
    if weakness and not fever:
        print("Take a rest")
    else:
        print("You may be cold")
print("END")

print()
print("Zad 2 version2")
musclePain= False
fever = False
weakness = True
if not musclePain and fever and weakness:
    print("suspicion of influenza")
elif not(fever or musclePain) and weakness:
    print("take rest")
else:
    print("you may be cold")
print("END")
print()
print("Zad 3 - mezczyzna przechodzi przeziebienie jak grype")

isMan = False
musclePain= False
fever = False
weakness = False

if (musclePain and fever and weakness) or (isMan and (musclePain or fever or weakness)):
    print("suspicion of influenza")
elif not(fever or musclePain) and weakness:
    print("take rest")
else:
    print("you may be cold")
print("END")
print()

