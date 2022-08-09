n=int(input("Enter the number of elements you want in the list: "))
print("Enter the elements:\n")
l=[]
c=0
for i in range(n):
    l.append(input())
for i in l:
    if i.isdigit()==True:
        c+=1
print("Number of digits = ",c)
