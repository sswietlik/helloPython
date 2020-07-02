persons = ['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margatet','Svetlana@mycompany.eu','Raphael']

domain = 'mycomapny.com'

emails = []
# VERSJA 1
# for person in persons:
#     if '@' in person:
#         emails.append(person)
#     else:
#         email = person+'@'+domain
#         emails.append(email)
#
# for email in emails:
#     print(email)
# VERSJA 2
for person in persons:
    if '@' in person:
        emails.append(person)
        continue

    email = person + '@' + domain #jeśli jednak IF się nie wykonało to tworzę mail
    emails.append(email)         # a nastepnie listę emails powiększam o stworzony adres mailowy

for email in emails:
    print(email)