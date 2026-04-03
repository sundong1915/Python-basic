for i in range(1,6):
    print('hello')

def greet(x):
   for j in range(1,x+1):
    print('nice to meet you')

greet(4)

def exp(a,b):
    mul=1
    for i in range(1,b+1):
     mul*=a
    print(mul)

exp(5,6)