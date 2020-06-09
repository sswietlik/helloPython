Tax = (4,7,8,23)
print(Tax[-1])
print(Tax.index(7))
print(Tax.count(8))
print(max(Tax))  #jaka jest maksymalna wartosc w TAX ?

TaxList = list(Tax) #konwersja TUPLE na LISTę
TaxList.append(30)
NewTax = tuple(TaxList) #tworzymy TUPLE z istniejącej listy

print(Tax)
print(TaxList)
print(NewTax)

(tax1,tax2,tax3,tax4) = Tax #za pomocą jednego przypisania inicjuję kilka zmiennych
print(tax1,tax2,tax3,tax4)
print()
a=1
b=10
print("a = ",a,"\tb =",b)

a=b
b=a
print("a = ",a,"\tb =",b)
print()

print('użycie zmiennej tymczasowej')
a = 1
b = 10
print("a = ", a, "\tb =", b)
temp=a #użycie zmiennej tymczasowej
a = b
b=temp
print()

print('opcja 3 z uzyciem tuple')
a = 1
b = 10

(a,b)=(b,a)
print("a = ", a, "\tb =", b)