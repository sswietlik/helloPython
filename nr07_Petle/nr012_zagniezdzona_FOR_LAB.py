n=10
tmp=1

for j in range(1,n+1):
    tmp *= j
    print(n,tmp)

print('-----------------------------------------')

x=10
for i in range(1,x+1):
    tmp= 1
    for j in range(1,i+1):
        tmp *= j
        print(i,tmp)

print('-----------------------------------------')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(adj,noun)