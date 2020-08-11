filename = '/home/slavo/temp/data_input/output.txt'

line = 'Europe'
cities = ['London','Berlin','Paris','Warsaw','Madrid','Rome']
# file = open(filename,'w')   #użycie W zapisuje plik od zera ,
file = open(filename, 'a')  # użycie A pozwala na dopisywaine do już istniejącego pliku
# file =open(filename,'w+')
# file =open((filename,'a+'))
file.write(line)
file.write('\n')
# file.writelines(cities)

for city in cities:
    file.write(city+'\n')

file.close()