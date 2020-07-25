import geom


# def GiveGeomSeqElement(a1=2, factor=2, index=2):
#     # returns n-th term of geometric sequence starting with element a1 and having
#     value = a1 * pow(factor, index - 1)
#     return value
#
#
# def GiveFactorForGeomSeq(term, nextterm):
#     # returns factor for geometrical sequence having two following terms of the sequence
#     return nextterm / term
#
#
# def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
#     # returns sum of n first elements of geometrical sequence with first term a1 and factor
#     sumN = a1 * (1 - pow(factor, n)) / (1 - factor)
#     return sumN


print('2^64 = ', geom.GiveGeomSeqElement(1,2,64))

a1=3
factor=2
maxindex=11

for i in range(1,maxindex):
    an = geom.GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term',i, '= ',an)

print('Factor is ', geom.GiveFactorForGeomSeq(12,24))
print('------------------')
print('Sum of n elements is ', geom.GiveSumOfNElementsGeomSeq(2,3,4))
