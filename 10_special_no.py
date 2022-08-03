n=int(input("Enter a number: "))
num=n
f=1
s=0
while n!=0:
    d=n%10
    for i in range(1,d+1):
        f=f*i
    s=s+f
    f=1
    n=n//10
if s==num:
    print("Special Number")
else:
    print("Not a Special Number")