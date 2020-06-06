q = "THE EYES"
print(q[0:7])
print(q)
print(q[0],q[1],q[2],q[3],q[4],q[5],q[6])
print(q[0]+q[1]+q[2]+q[3]+q[4]+q[5]+q[6])
print()

q="a gentleman"
print(q)
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])
print()

q="THE MORSE CODE"
print(q[1:3],q[6],q[2],q[3],q[10:12],q[4],q[13],q[9],q[12],q[5],q[0],q[7])
print(q[1:3]+q[6]+q[8]+q[3]+q[10:12]+q[4]+q[13]+q[9]+q[12]+q[5]+q[0]+q[7])
print()

line='Program "Kropka nad i" nadamy o: 22:00'
time=line[line.find(':')+2:]
print(time)

tmp=line[line.find('"')+1:]
tmp2=tmp[:tmp.find('"')]
print(tmp2," :",time)

#print(tmp[:tmp.find('"')])
# print(message[message.find(':')+2:])



