i=0

for i in range(1,10):
    if i%2==1: continue
    print(7*i,end=' ')

print()

j=0

for j in range(1,101):
    if j%2==0 or j%3==0: 
        continue
    print(j)

print()

k=0

while k<101:
    if k%2!=0 and k%3!=0:
         print(k)
    k+=1
