str1=input("Enter 1st string: ")
str1=str1.lower()
str2=input("Enter 2nd string: ")
str2=str2.lower()
if sorted(str1)==sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")