n=int(input("Enter the number of elements you want in the list: "))
print("Enter the elements:\n")
l=[]
dl=[]
for i in range(n):
    l.append(input())
for i in l:
    if i not in dl:
        dl.append(i)
print("Original list: ")
print(l)
print("After removing duplicates: ")
print(dl)