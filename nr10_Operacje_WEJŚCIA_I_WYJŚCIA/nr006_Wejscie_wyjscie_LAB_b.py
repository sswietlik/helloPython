import os
filename = input('Enter filename wit web addresses to read: ')
while not os.path.isfile(filename):
    print('File does not exist. Try again: ')
    filename = input("Enter filename to read:")
webadresses = []
with open(filename,"r") as file:
    for line in file:


