n=int(input("Enter the number of elements you want in the list: "))
print("Enter the elements:\n")
l=[]
for i in range(n):
    l.append(int(input()))
print("Original list:\n")
print(l)
temp=l[0]
l[0]=l[n-1]
l[n-1]=temp
print("\nFinal list:\n")
print(l)