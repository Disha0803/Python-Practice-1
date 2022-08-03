n=int(input("Enter a number: "))
num=n
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
if rev==num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")