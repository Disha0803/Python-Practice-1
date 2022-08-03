n=int(input("Enter a number: "))
num=n
an=0
while n!=0:
    d=n%10
    an=an+d**3
    n=n//10
if an==num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")