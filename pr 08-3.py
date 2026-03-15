for i in range(1,10):
    if i%2==0:continue
    print(7*i,end=' ')

print()

for j in range(2,100):
    if j%2==0 or j%3==0:continue
    print(j,end=' ')

print()

for k in range(2,100):
    if k%2!=0 and k%3!=0:
     print(k,end=' ')