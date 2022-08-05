from audioop import reverse


str=input("Enter a string: ")
str=str.upper()
rev=str[::-1]
if str==rev:
    print("Palindrome String")
else:
    print("Not a Palindrome String")