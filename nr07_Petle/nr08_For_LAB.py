data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for dataError in data:
        print('\n'+dataError.upper())
print('----------------------------------------------')

for dataError in data:
        splitElements = dataError.split(':')
        print(splitElements[0].upper(),'\n',splitElements[1])
print('----------------------------------------------')

for dataError in data:
        splitElements = dataError.split(':')
        if splitElements[0]=='Error':
                print(splitElements[1].upper())
        else:
                print(splitElements[1])
