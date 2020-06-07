message1 = 'Processing file %s'
print(message1 % ('file_1.txt'))
print()

message2 = 'File %s has size %d KB' # message2(%s,%d)
print()
print(message2 % ('file2_jpg',100)) #W tym przypadku po % (ma wyświelić nazwę pliku, oraz rozmiar)
print()

message3 = 'File %20s has size %10d KB'
print(message3 % ('file3.txt',100))
print('dla nazwy pliku zarezerwowano nazwę 20sto znakową dlatego program wyświetla pustą przestrzeń')
print('to samo tyczy sie wyswietlanej dlugosci rozmiaru pliku')
print()
message4 = 'Processing file{0:s}'
print(message4.format('file4.txt')) #inny sposób przekazywania powyższych informacji
print()
message5 = 'File {0:s} has size {1:d} ' #{0:s} - 0 czyli miejsce zerowe , {1:d} - 1 czyli miejsce pierwsze

print(message5.format('file5.txt',100))
print()
print('zmieniam kolejnosci użycia w nawiasach klamrowych')
message6 = 'File {1:s} has size {0:d}'
print(message6.format(100,'file.xxx'))
print()

message7 = 'File {1:20s} has size {0:10d}'
print(message7.format(100,'file7.txt'))

