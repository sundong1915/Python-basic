st=[1,2,3,4]
print(st[0])
print(st[-2])

st[0]+=1
print(st)

for i in range(0,4):
    st[i]+=1

print(st)

st1=[1,2,3,4,5,6]
st1[0],st1[1]=st1[1],st1[0]
print(st1)