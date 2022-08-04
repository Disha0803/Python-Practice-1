n=int(input("Enter a number: "))
f=0
while n!=0:
    d=n%10
    if (d!=0 and d!=1):
        f=1
        break
    n=n//10
if f==0:
    print("Binary Number")
else:
    print("Not a Binary Number")