def main():
    num=int(input("num: "))
    if num>0:
     print("above 0")
    else:
       print("under 0")

main()

def main2():
    num=int(input("num2: "))
    if num>1 and num<5:
     print("True")
    else:
       print("False")

main2()

num3=12

if num3<3 or num3>10:
   print("Good")
else:
   print("Not good")

num4=4

if num4%2==0:
  if num4%3!=0:
     print("correct")
else: print('not correct')