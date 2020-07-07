import random
print()

print('One random number:', random.randint(1,100)) #losowanie lczby całkoitej (działa to w pełnym zakresie)
print()


print('Choosing random number from a range', random.choice(range(1,100)))
print()

print('Choosing random number from a range-easier way', random.randrange(1,100))
print()

list=['John','Ann','Peter','Susan','Emily','Greg','Chris']
print('Oryginal list :',list)
random.shuffle(list)
print('Reordered list:',list)
print()

