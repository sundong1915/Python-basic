st=[]
st.append(1)
st.append(2)
st.append(3)

print(st)

st.remove(1)
st.remove(2)
st.remove(3)

print(st)

st=[]
st.append(1)
st.append(2)
st.append(3)

print(st)

st.pop(1)

print(st)

st1=[1,2,3,4]
st1[:]=[0]

print(st1)

st4=[]
for i in range(1,11,1):
    st4.append(i)

print(st4)

for j in range(1,11,1):
    st4.remove(j)

print(st4)

st5=[1,2]
st5[2:4]=[3,4,5]
print(st5)