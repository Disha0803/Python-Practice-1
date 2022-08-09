n=int(input("Enter the number of elements you want in the list: "))
print("Enter the elements:\n")
l=[]
for i in range(n):
    l.append(input())
newlist=l.copy()
print("Copied list: ")
for i in newlist:
    print(i,end=',')
