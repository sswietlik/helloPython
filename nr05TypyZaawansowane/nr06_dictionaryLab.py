print()

chanels= {'Google':'1480','Email':'300','Natural Traffic':'440','TV Sport':'700'}
print('Chanels_Dictionary')
print(chanels)
print()

print(chanels['Email'])
print()

chanelsUpdate={'Natural Traffic':'520','News':'600'}
print(chanelsUpdate)
print()

chanels.update(chanelsUpdate)
print('Aktualizacja chanels')
print(chanels)
print()

print(chanels.keys())
chanels.pop('Email')
print('chanels po usunieciu wartości Email')
print(chanels)