persons = ['Elizabeth','Steven','Sebastian','Margatet','Svetlana','Raphael']
domain = 'mycompany.com'

for person in persons:
    email = person + '@'+domain
    print('Email for\t',person,'\tis\t',email)
else:
    print('\t\t\tend of the list')