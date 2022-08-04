n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
if n1<n2:
    l=n1
else:
    l=n2
for i in range (1,l+1):
    if ((n1%i==0) and (n2%i==0)):
        gcd=i
print("The GCD = ",gcd)