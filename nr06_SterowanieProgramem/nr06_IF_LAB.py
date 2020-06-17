print('IF-LAB')
print('zad 1')
print('tworze zmienne :'+ 'musclePain, fever, weakness')

musclePain = False
fever = True
weakness = False
print()
print('zad 2')
if musclePain and fever and weakness:
    print('suspicion of influenza')
else:
    print('The flu is unlikely')
print()

print('zad 3')
if musclePain and fever and weakness:
    print('suspicion of influenza')
elif weakness and not (fever or musclePain):
    print('Just take a rest!')
else:
    print('you may be cold')
print()

print('zad 4')
print('dodaje MĘską zmienną isMan')
isMan = False
print()

print('zad 5')
if musclePain and fever and weakness:
    print('suspicion of influenza')
elif isMan and (musclePain or fever or weakness):
    print('suspicion of influenza')
elif weakness and not (fever or musclePain):
    print('Just take a rest!')
else:
    print('you may be cold')
print()

print('zad 6')

isCheckCompleted = False
print('CheckListCompledet' if isCheckCompleted else 'CHECK NOT DONE YET!' )





