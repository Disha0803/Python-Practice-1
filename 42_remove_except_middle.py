n=int(input("Enter the number of elements you want in the list: "))
print("Enter the elements:\n")
l=[]
for i in range(n):
    l.append(input())
print("Original list:")
print(l)
m=n//2
mid1=l[m]
mid2=l[m-1]
l.clear()
print(l)
if n%2==0:
    l.append(mid1)
    l.append(mid2)
else:
    l.append(mid1)
print("Final list:")
print(l)