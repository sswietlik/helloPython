hitsTitles=['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
print(hitsTitles)

hitsTitles.append(('CHILD IN TIME'))
hitsTitles.append(('AGAIN'))
print(hitsTitles)

hitsTitles.insert(2,'HOTEL CALIFORNIA')
print(hitsTitles)

hitsTitles.insert(0,'THE SOUND OF SILENCE')
print(hitsTitles)

print(hitsTitles.index('HOTEL CALIFORNIA'))

hitsTitles.remove(('HOTEL CALIFORNIA'))
print(hitsTitles)

hitsTitles.remove(('THE SOUND OF SILENCE'))
hitsTitles.insert(0,'ENJOY THE SILENCE')
print(hitsTitles)
print()
print('kopia edytowalna listy glownej')
hitsToRead = hitsTitles.copy()
print(hitsToRead)

hitsToRead.reverse()
print(hitsToRead)

hitsToRead.sort()
print(hitsToRead)

print(hitsToRead.pop(0),",",hitsToRead.pop(0))
print(hitsToRead)

additionalSongs=['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
print(additionalSongs)
hitsToRead.extend(additionalSongs)
print(hitsToRead)

print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))

hitsToRead.clear()
print(hitsToRead)

print(hitsTitles)
print(hitsToRead)
print(additionalSongs)



