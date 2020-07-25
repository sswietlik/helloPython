print('------------Zad 1------------')
def GiveGeomSeqElement(a1=2,factor=2,index=2):

    value = a1*pow(factor,index-1)
    return value

print('element 64 = ', GiveGeomSeqElement(1,2,64))
#Wylicz wartość 64 elementu ciągu geometrycznego,
# którego pierwszym elementem jest 1 a współczynnik wynosi 2

print('------------Zad 2------------')
a1=3
factor=2
maxindex=10

for i in range(1,maxindex):
    an = GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term',i,an)
print('------------Zad 3------------')

def GiveFactorForGeomSeq(term,nextterm):
    value=nextterm/term
    return value
print(GiveFactorForGeomSeq(12,24))

print('------------Zad 3------------')

def GiveSumOfNElementsGeomSeq(a1=2,factor=2,n=2):
    sumNx = a1 * (1 - pow(factor, n)) / (1 - factor)


    #       a1*(1-q^n)
    # Sn = ------------
    #          1-q

    sumN = (a1*(1-pow(factor,n)))/(1-factor)
    return sumN,' myfunction versus udemy function',sumNx
print(GiveSumOfNElementsGeomSeq(2,3,4))
print()









