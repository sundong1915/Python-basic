def divide(a,b):
    answer=int(a/b)
    
    remains=int(a%b)
    print('answer=',answer,'remains=',remains)

divide(5,2)

def sum(c,d):
    collect=0
    for i in range(c+1,d):
     collect+=i
    
    print(collect)

sum(1,5)