print('Zad 1')
print()
cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9] #ciężar paczek
print('Lista Cargo : ',cargo)
cargo.sort()
cargo.reverse()
print('Sortowana Lista Cargo',cargo)


boxCapacity = 90 #ładowność pudla
box = []
i = 0

while i<len(cargo) and (boxCapacity - sum(box)) >= min(cargo):
    if (boxCapacity -sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print('The collected items sum is : ', sum(box))
print('The elements are : ', box)


