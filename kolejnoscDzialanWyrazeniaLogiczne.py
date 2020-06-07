nrButa=45
stalaTwardowskiego=5
zmiennaTwardowskiego=50
kFactor=20
yFactor=1020
yBorn=1984

result=(((nrButa*stalaTwardowskiego+zmiennaTwardowskiego)*kFactor)+yFactor)-yBorn
print(result)

print()

lCalkowita=8
multiple=2
addFactor=10
divide=2
negative=8

result=((lCalkowita*multiple+addFactor)/2)-lCalkowita
print(result)

print(2+2*2)

print(7+7/7+7*7-7)

obecnosc80=True
gradeMin3=True
finishedTopic=True

passSchool = obecnosc80 and gradeMin3 and finishedTopic
print(passSchool)

print()

obecnosc = 0.85
note = 3.0
finalWorkOk = True

print('Zdales', obecnosc==0.85 and note>=3.0 and finalWorkOk)
print('nie zaliczone', obecnosc<=0.4 and note>=3.0 and finalWorkOk)

print()
print("zmienil zdanie")
obecnosc = 0.80
note = 3.0
finalWorkOk = True

print('Praca do poprawki', obecnosc==0.80 and note>=3.0 and finalWorkOk!='')
print('Zdales', obecnosc>=0.80 and note>=3.0 and finalWorkOk)

print()
print("student ma")
obecnosc = 0.8
note = 3.0
finalWorkOk = True

print('nie zalicza', obecnosc==0.40 and note>=2.5 and finalWorkOk=='')
print('Zdales', obecnosc>=0.80 and note>=3.0 and finalWorkOk)




print()
presence = 0.85
note =3.5
finalWorkOK = False
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)
presence = 0.4
note =2.5
finalWorkOK = True
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)