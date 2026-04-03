def divide(a,b):
    c=int(a/b)
    d=a%b

    print(c)
    print(d)

divide(9,2)

def addup(x,y):
    sum=0
    for i in range (x,y+1):
     sum=sum+i
    print(sum)
    
addup(5,9)