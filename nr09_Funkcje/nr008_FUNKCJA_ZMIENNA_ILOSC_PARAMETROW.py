print('______________Version1______________')
def DoAction(action,parameter):
    print('action: ',action)
    print('parameter: ',parameter)
    return

DoAction('buy','shoes')




print('______________Version2______________')

def DoAction2(action,*parameter):
    # * gwiazdka oznacza to co przychodzi do funkcji nie jest poj
    # elementem ale kolekcją czyli TUPLE
    # GWIZDKA JEST RODZAJEM SEPARATORA który mówi że przechodzimy do Listy, Tuple czy jakiś innych zbiorow wartosci

    print('action: ',action)
    print('parameter: ',parameter)
    for element in parameter:         #wyświetlam z osobna wszystkie elementy dla TUPLE
        print('element is :',element) #wyświetlam z osobna wszystkie elementy
    return
DoAction2('buy','shoes','socks')
DoAction2('buy','shoes','socks','T-Shirt')





print('______________Version3______________')

def DoAction3(action,what, **parameter):

    print('action: ',action)
    print('what: ',what)
    print('parameter: ',parameter) # parameter stał się po poniższej zmianie SŁOWNIKIEM
    for element in parameter:
        print(element, '=', parameter[element])
    return
DoAction3('buy','shoes',size=45,color='brown',type='sport')
