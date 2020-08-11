import os

webadresses = []

line = input('Enter web adress like "www.python.org or press ENTER to stop:  ')
while line != '':
    webadresses.append(line)
    line = input('Enter web adress like "www.python.org or press ENTER to stop:  ')

print(webadresses)

dirname = os.getcwd()
print(dirname)
filename = input('Enter file name ')
filepath = os.path.join(dirname,filename)
file = open(filepath, 'w+')
for webadress in webadresses:
    file.write(webadresses+"\n")
    file.close()


