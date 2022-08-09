n=int(input("Enter the number of elements you want in the list: "))
print("Enter the elements:\n")
l=[]
f=0
for i in range(n):
    l.append(int(input()))
s=l[0]
for i in l:
    if i>s:
        s=i
print("The largest element is: ",s)