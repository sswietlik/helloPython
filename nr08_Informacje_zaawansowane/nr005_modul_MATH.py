f_smaller = 3.141592653589793
f_bigger = 3.87756392764

import math
print()

print('math.CEIL() czyli najmniejsza liczba całkowita większa od danej liczby')
print('\n',math.ceil(f_smaller),'\n',math.ceil(f_bigger))
print()

print('FLOOR zwraca liczbę najwięszką  najmniejszą całkowitą od podanego arugmentu')
print('\n',math.floor(f_smaller),'\n',math.floor(f_bigger))
print()

print('math.CEIL() czyli najmniejsza liczba całkowita większa od danej liczby \nw tym przypadku względem liczby ujemnej')
print('\n',math.ceil(-f_smaller),'\n',math.ceil(-f_bigger))
print()

print('FLOOR zwraca liczbę najwięszką  najmniejszą całkowitą od podanego arugmentu,\nw tym przypadku względem liczby ujemnej')
print('\n',math.floor(-f_smaller),'\n',math.floor(-f_bigger))
print()

print('czyli podnoszenie do potęgi 2 do potęgi 8 , oraz pierwiastkowanie 9 do potęgi 0,5')
print(pow(2,8),' ',pow(9,0.5))
print()

print('pierwiastek kwadratow')
print(math.sqrt(16))
print()

print('można używać stałe typu Pi , E')
print(math.pi,' ',math.e)
print()


