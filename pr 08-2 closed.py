lcm=0

while True:
    lcm+=1
    if lcm%6==0 and lcm%45==0:
        break
    
print(lcm)

gcd=120

while True:
    gcd-=1
    if 120%gcd==0 and 42%gcd==0:
        break
    
print(gcd)