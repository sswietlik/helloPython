IsWeekend = True   #narzucam wartość logiczną
print("Is weekend =", IsWeekend)

Temperature =25
print("Temperature =", Temperature)

ToDoList = ''
print("ToDoList =",ToDoList)
print()

IsHappy = IsWeekend and Temperature >=20 and ToDoList==''
print("IsHappy =",IsHappy)
print()

IsHappy = not IsWeekend and Temperature < 20 and ToDoList !=''
print("IsHappy =",IsHappy)
print()
IsHappy = IsWeekend and Temperature >=20 and ToDoList =='' \
    or not IsWeekend and Temperature < 20 and ToDoList !=''
print("IsHappy = ", IsHappy)
print()

IsHappy = IsWeekend and Temperature >=20 and ToDoList =='' \
    or not IsWeekend and not (Temperature < 20 and ToDoList !='')
# w powyższym przykładzie priorytet ma NAWIAS potem NOT pote AND a najsłabszy OR
print("IsHappy = ", IsHappy)
