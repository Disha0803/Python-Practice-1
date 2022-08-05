str=input("Enter a string: ")
r=''
char=input("Enter a character to replace the string space: ")
for i in str:
    if i==' ':
        i=char
    r+=i
print(r)