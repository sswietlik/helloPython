marketing=['loyality program','client promotion','market research']
print(marketing)
print()

marketing.append('public relations')
print(marketing)
print()

print(marketing[3])
print()

marketing.insert(2,'investor relations')
print(marketing)
print()

emailMarketing=marketing.copy()
print('Lista org nr1')
print(marketing)
print()
print('Lista cop nr2')
print(emailMarketing)
print()

emailMarketing.sort()
print(emailMarketing)
print()

internalEmail=['internal communication']
print('Lista cop nr3')
print(internalEmail)
print()

emailMarketing.extend(internalEmail)
print(emailMarketing)

tupleEmailMarketing = tuple(emailMarketing)
print(tupleEmailMarketing)



