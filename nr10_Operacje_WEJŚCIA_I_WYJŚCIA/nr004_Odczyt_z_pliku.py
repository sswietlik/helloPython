print('----------------ODCZYT WERSJA 1----------------')
file = open('/home/slavo/temp/data_input/orders.csv','r')

content = file.read()
print(content)

file.close()


print('----------------ODCZYT WERSJA 2----------------')
with open('/home/slavo/temp/data_input/orders.csv','r') as file:
    content = file.read()
    print(content)


print('----------------ODCZYT WERSJA 3----------------')
print('----------------LINIJKA PO LINIJCE----------------')
with open('/home/slavo/temp/data_input/orders.csv','r') as file:
    for line in file:
        print(line)

print('----------------ODCZYT WERSJA 4----------------')
file = open('/home/slavo/temp/data_input/orders.csv','r')
for line in file:
    print(line)
file.close()


print('----------------ODCZYT WERSJA 5----------------')

file = open('/home/slavo/temp/data_input/orders.csv','r')

fragment = file.read(10)        # chcemy przeczytać na raz max 10bitów
while fragment:                 # sprawdzam czy coś zostało odczytane
    print(fragment)             # jeśli tak to wyświetlamy to co odczytało
    fragment = file.read(10)    # następnie przechodzimy do odczytu kolejnych 10bitów
file.close()                    # jesli niema już nic do odczytu to pentla się kończy

print('----------------ODCZYT WERSJA 5-- z uzyciem wskaznika gdzie sie znajdujemy--------------')

file = open('/home/slavo/temp/data_input/orders.csv','r')

fragment = file.read(10)        # chcemy przeczytać na raz max 10bitów
while fragment:                 # sprawdzam czy coś zostało odczytane
    print(file.tell(),fragment)             # jeśli tak to wyświetlamy to co odczytało
    fragment = file.read(10)    # następnie przechodzimy do odczytu kolejnych 10bitów
file.close()                    # jesli niema już nic do odczytu to pentla się kończy
