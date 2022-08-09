n=int(input("Enter the number of elements you want in the list: "))
print("Enter the elements:\n")
l=[]
for i in range(n):
    x=input()
    if x!="":
        l.append(x)
if l==[]:
    print("Empty list")
else:
    print("Not empty")