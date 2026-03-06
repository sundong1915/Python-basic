def sum(list):
    add=0
    for i in list:
        add+=i
    
    print(add)

st=[1,2,3,4,5]

sum(st)

def reverse(list):
    for i in range(len(list)-1,-1,-1): #not using reverse
     print(list[i])

reverse(st)