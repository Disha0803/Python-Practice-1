n=int(input("Enter a number: "))
num=n
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")