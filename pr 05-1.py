st=[1,2,3,4]

for i in st:
 print(i)

for j in range (len(st)-1,-1,-1):
 print(st[j])

st2=[1,2,3,4]

for k in range(len(st2)):
 st2[k]+=1
 print(st2[k])

st3=[1,2,3,4]
st3[0], st3[3]=4,1

print(st3[0],st3[3])