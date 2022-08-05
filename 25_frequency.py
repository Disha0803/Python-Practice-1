str=input("Enter a string: ")
str=str.lower()
str=str.replace(" ",'')
f={}
for i in str:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1
r=max(f, key=f.get)
print("Highest frequency character: ",r)