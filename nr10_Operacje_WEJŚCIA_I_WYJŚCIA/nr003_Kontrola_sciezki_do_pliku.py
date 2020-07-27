import os


while True:

    fileName = input('enter pat to results files : ')

    if os.path.isfile(fileName):
        break
    else:
        print('File name is not correct, try again !')


print('The results file is %s' % (fileName))
