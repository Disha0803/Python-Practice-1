n=int(input("Enter the number of elements you want in the list: "))
print("Enter the elements:\n")
l=[]
f=0
for i in range(n):
    l.append(int(input()))
key=int(input("Enter an element you want to search: "))
for i in l:
    if key==i:
        f=1
        break
    else:
        f=0
if f==1:
    print("Element found")
else:
    print("Element not found")