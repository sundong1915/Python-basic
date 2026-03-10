def main():
    num=int(input("input: "))
    if num<=0:
      print("smaller than 0")
    else:
      print("bieer than 0")

main() 

num2=int(input("input num 1<num<5:"))
if 1<num2<5:
   print("1<number<5")
else:
   print("wrong number")

num3=int(input("input num 3>num, num>10:"))
if 1<num2<5:
   print("3>num, num>10")
else:
   print("wrong number")

num4=int(input("input num%2==0, %3!=0:"))
if num4%2==0 and num4%3!=0:
   print("num%2==0, %3!=0")
else:
   print("wrong number")