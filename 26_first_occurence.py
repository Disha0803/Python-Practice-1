str=input("Enter a string: ")
nstr=''
c=0
for i in str:
    if (c!=1):
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            i='-'
            nstr=nstr+i
            c=1
        else:
            nstr=nstr+i
    else:
        nstr=nstr+i

print("The new string is: ",end='')
print(nstr)