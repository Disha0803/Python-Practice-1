from functools import reduce
def addall(x,y):
    return x+y
l=[1,2,3,4,5]
data=reduce(addall,l)
print(data)