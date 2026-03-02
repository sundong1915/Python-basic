for i in range(0,5):
    print("hello",end=' ')

print()

for j in range(7,64,7):
 print(j,end=' ')

print()

def pr1(a,b):
   result=1
   for c in range(b):
    result=result*a
 
   return result

f_result=pr1(3,5)
print(f_result)

def greet():
  for k in range(cnt):
    print("nice to meet you")

cnt=int(input("How many times: "))

greet()
