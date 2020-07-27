# filename = input('Enter filename: ')
#
# print('The file name is %s' % (filename))

# filesize = input('enter the max file size: ')
# print('the max size is %d' % (filesize))
# print('the max size is %s' % (filesize))

# print('Size in KB is %s ' % (filesize*1024))
#w powyższym przyapdku Python powiela naszą wskazaną liczbę * 1024 razy

while True:


    filesizeSTR = input('enter the max file size (MB) : ')
    if filesizeSTR.isdecimal():
        filesizeInt = int(filesizeSTR)
        break


print('the max size is %d' % (filesizeInt))
print('Size in KB is %d ' % (filesizeInt*1024))






#   %D oznacza DECIMAL czyli liczbę
#   %S oznacza STRINg czyli napis
# print('Size in KB is %s ' % (filesize*1024))

