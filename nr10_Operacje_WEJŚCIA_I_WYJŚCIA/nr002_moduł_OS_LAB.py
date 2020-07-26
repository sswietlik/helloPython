import os
import time


dir = input('podaj ścieżkę dostępu do katalogu')

if not os.path.isdir(dir):
    print('%s must be a directory' % dir)
else:
    file = input('Wprowadź nazwę pliku :' % dir)
    path = os.path.join(dir,file)

    if not os.path.isfile(file):
        print('file not exist')    #print('File %s does not exist!' % path)
    else:
        print('data ostatniej modyfikacji pliku', os.path.getmtime(file))

        print('rozmiar pliku w bajtach', os.path.getsize(file))

        print('bieżący katalog ', os.getcwd(file))

        print('podaje ścieżkę względna pliku', os.path.abspath(file))


