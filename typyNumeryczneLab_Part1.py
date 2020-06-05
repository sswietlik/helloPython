name='Slawek'
print(name)
age=36
print(age)
daysInYear=365
print(daysInYear)
message= "%s is %d years old, so is about %s days old"
print(message % (name,age,daysInYear*age))
print()
name='Beata'
age=30
print(message % (name,age,daysInYear*age))
print()
print("użycie formatowania")
name='Slawek'
age=36
message='{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,daysInYear*age))
name='Beata'
age=30
print(message.format(name,age,daysInYear*age))
print()
num1=1234567890
num2=12345

message= "%s divided by %d is %s and the reest is %d"
print(message %(num1,num2,num1//num2,num1%num2))
