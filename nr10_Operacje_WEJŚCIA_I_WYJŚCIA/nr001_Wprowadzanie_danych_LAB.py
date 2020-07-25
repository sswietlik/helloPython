def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

print('This program solves equation ax^2+bx+c = 0')
print('Enter the valued for a, b, c : ')

a_str = input('a=')
b_str = input('b=')
c_str = input('c=')

if not (check_int(a_str) and check_int(b_str) and check_int(c_str)):
    print('a,b,c need to be int!!!')
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)

    if a == 0:
        print('a cannot be 0!!')
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('no solution')
        elif delta == 0:
            x1 = ((-b-delta**0.5)/2*a)
            print(x1)
        else:
            x1 = ((-b-delta**0.5)/(2*a))
            x2 = ((-b+delta**0.5)/(2*a))
            print('x1 =',x1, ' ', 'x2 = ',x2)




# y=a*(x^2) + b*x + c
