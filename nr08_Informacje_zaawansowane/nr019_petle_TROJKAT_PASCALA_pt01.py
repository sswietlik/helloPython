# numbers =[1]
# print(numbers)
# for i in range(5):
#     newNumbers = [1]
#     position = 0
#     len(numbers)
#     print(len(numbers))
#
#     while position < len(numbers) -1:
#         newNumbers.append(numbers[position]+numbers[position+1])
#         position += 1
#     newNumbers.append(1)
#     numbers =newNumbers.copy()
#     print(numbers)
print('wersja 2 ')
def pascalSpot(row,col):
    if (col == 1): return 1
    if (col == row): return 1
    upLeft = pascalSpot(row-1,col -1)
    upRight = pascalSpot(row-1,col)
    return upLeft + upRight
for r in range(1,6):
    for c in range(1,r+1):
        print(pascalSpot(r,c),end =' ')
    print('')