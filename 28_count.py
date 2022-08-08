str=input("Enter a string: ")
sc=0
a=0
d=0

for i in str:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        d+=1
    else:
        sc+=1
print("Number of alphabets= ",a)
print("Number of digits= ",d)
print("Number of special characters= ",sc)