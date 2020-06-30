string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(1,11):
    print(string_A)


print('_______________________________________________________________________')
print()

for i in range(1,10):
    if i %2 == 0:
        print(string_B)
    else:
        print(string_A)
print('_______________________________________________________________________')
print()


for i in range(1,10):
    print('x'*i)

print('_______________________________________________________________________')
print()

for i in range(1,10):
    if i %2 ==0:
        print('x'*i)
    else:
        print('o'*i)