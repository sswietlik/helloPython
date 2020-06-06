s="A Python script"

# A PYTHON SCRIPT
# 012345678901234
print(s[0])
print(s[2])
print(s[2:7])
print(s[2:8])
print(s[:8]) #POZWALA NA ZASSANIE ZNAKÓW OD 0 DO 8
print(s[8:]) #POZWALA NA ZASSANIE ZNAKÓW OD 8 DO KONCA
print(s[2:9999999])
print(s[222:99999])

message = 'Document "cv.doc" was printed on printer: XEROX'
print(message.find(':'))
print(message[message.find(':'):])
print(message[message.find(':')+2:])
print(message[message.find('"')+1:]) #szukamy w message znak "
                                    # a nstępnie od następnego znaku program wypluwa reszte wiadomosci
print()

tmp = message[message.find('"')+1:] #Tworzę zmienną tymczasową o zawartości wcześniej wyszukanych wartości
print(tmp)
print(tmp[:tmp.find('"')]) #teraz w tmp odszukujemy lokalizację " i wybieramy wszystko od początku teksu
#należącego do TMP aż do drugiego cudzysłowia
