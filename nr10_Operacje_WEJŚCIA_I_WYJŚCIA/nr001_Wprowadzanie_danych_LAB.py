def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

print('program do rozwiązania równania kwadratowego')
print()

print('podaj współczynnik  A B oraz C')
A_str = input('A=')
B_str = input('B=')
C_str = input('C=')

#jeśli a lub b lub c nie są liczbami całkowitymi,
# to należy wyświetlić odpowiednią informację i zakończyć skrypt
if not check_int(A_str) and check_int(B_str) and check_int(C_str):
    print('Wspołczynniki A B oraz C nie są liczbami całkowitymi')

#sprawdzam czy są liczbami całkowitymi
else:
    A = int(A_str)
    B = int(B_str)
    C = int(C_str)

    if A==0:
        print('to nie jest równanie kwadratowe')
    else:
        delta = B**2 - 4*A*C
        if delta <0:
            print('Delta < 0 - brak rozwiązania')
        elif delta == 0:
            x1 = (-B -delta*0.5)/(2*A)
            print('X1 = ', x1)

        else:
            x1 = (-B -delta*0.5)/(2*A)
            x2 = (-B +delta*0.5)/(2*A)
            print('X1 = ',x1,'X2 = ',x2)



