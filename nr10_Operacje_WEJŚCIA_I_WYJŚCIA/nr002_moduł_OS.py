import os
import time
print('current directory is', os.getcwd())      #  podaje bieżący katalog

currentDir = os.getcwd()                        #sprawdzam ściężkę dostępu do pliku
filename = 'results.txt'                        #nadaję nazwę temu plikowi
fullpath = os.path.join(currentDir,filename)    #łączę ścieżkę dostępu z plikiem
print('\nThe constructed file pat is : ',fullpath)


#ścieżki do pliku mogą być względne lub bezwzględne

#ścieżka względna określa połozenie pliku względem bieżącego katalogu
relativePath = 'output.txt'                                     #szukam pliku OUTPUT.TXT
print('\nThe absolute path is :',os.path.abspath(relativePath)) #wyświetla ścieżkę bezwzględną


#ANALIZA ŚCIEŻKI

#Chcę WYODRĘBNIĆ nazwę pliku od katalogu i wyświetlić wyniki
filepath = r'/home/slavo/PycharmProjects/helloPython/nr10_Operacje_WEJŚCIA_I_WYJŚCIA/results.txt'
print('\nThe file name part is : ',os.path.basename(filepath))
print('The directory part is : ', os.path.dirname(filepath))

print('\nIs file existing ?:', os.path.exists(filepath))

if os.path.exists(filepath):
    print('nLast modif date is : ', os.path.getmtime(filepath))
    print('Last mdify date is : ', time.localtime(os.path.getmtime()))

    print('nFile size is :', os.path.getsize(filepath))

    print('nIs it a file ?',os.path.isfile(filepath))
    print('is it a dir ?',os.path.isdir(filepath))

    print('\nPath splitted:', os.path.split(filepath))
    print('only file name part: ',os.path.split(filepath)[1])

    print('\nPath splitted into drive :',os.path.splitdrive(filepath))
    print('only drive', os.path.splitdrive(filepath)[0])
