import os

file_path = r'/home/slavo/temp/data_input/orders.csv'


with open(file_path,'r') as file:
    for line in file:
        line = line.replace('\n', ' ') # usuwam linijkę przerwy między odczytanymi liniami
        order= line.split(',')
        print(order)
        if len(order) ==3:
            print('Order from drugstore "%s", item "%s", amount %s'% (order[0],order[1],order[2]))
        else:
            print('Line %s malformed !!!' % line)
        print('Processing finished')






