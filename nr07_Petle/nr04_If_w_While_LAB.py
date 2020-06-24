print('Zad 1')
print()

numbers = [8,18,2,4,16,5,25,4,22,3,3,5,3,9,81,11]

print('Trzeba odnaleźć takie dwie kolejne liczby,\nże druga jest kwadratem pierwszej.')
print()

i=0

max = len(numbers)-1
while i<max:
    print(i, '\t', numbers[i], numbers[i+1])
    if numbers[i+1] == numbers[i]**2:
        print('\t Found!')
    i+= 1
print()


print('Zad 2')
print('Interesuje nas odnalezienie takich 3 liczb, że \npierwsza do kwadratu równa się drugiej, \na druga do kwadratu równa się trzeciej. ')


i=0
max = len(numbers)-2
while i<max:
    print(i, numbers[i], numbers[i+1], numbers[i+2])
    if numbers[i]**2==numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
        print('Found@@')
    i+=1
print()

print('Zad 3')
print()

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i=0
max = len(texts)-1
while i< max:
    print(i, texts[i],texts[i+1])
    if len(texts[i]) == len(texts[i+1]):
        print('FOUND')
    i+=1