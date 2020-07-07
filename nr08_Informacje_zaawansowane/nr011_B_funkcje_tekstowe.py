line='this IS a very STRANGE text'
print(line.count('e')) #zliczam ile razy występuje literka 'E'
print(line.find('e')) #wyszukuje znak zaczynając OD STRONY LEWEJ
print(line.rfind('e')) #wyszukuje znak zaczynając OD STRONY PRAWEJ
print(line.index('e')) #wyszukuje znak zaczynając OD STRONY LEWEJ
print(line.rindex('e')) #wyszukuje znak zaczynając OD STRONY PRAWEJ
print(line.find('p')) #sprawdza CZY litera WYSTĘPUJE

print(line.startswith('this'))  #Bada czy funkcja rozpoczyna się lub kończy danyj ciągiem znaków
print(line.endswith('THIS'))
print(line.endswith('text'))

loren='''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'''
print(loren)
print()
print('użycie potrójnego cudzysłowa pozwala na automatyczne dorzucanie ''\ n ')
loren="""Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
  aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
   in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
     officia deserunt mollit anim id est laborum."""
print(loren)

print(loren.count('\n'))

